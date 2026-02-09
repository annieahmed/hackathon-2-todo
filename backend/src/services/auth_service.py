from sqlmodel import Session, select
from typing import Optional
from datetime import timedelta
from ..models.user import User, UserCreate, UserRead
from ..utils.password_utils import verify_password, get_password_hash
from ..utils.jwt_utils import create_access_token
from ..utils.responses import error_response, success_response


def authenticate_user(session: Session, email: str, password: str) -> Optional[User]:
    """
    Authenticate a user by email and password
    """
    statement = select(User).where(User.email == email)
    user = session.exec(statement).first()
    if not user or not verify_password(password, user.password_hash):
        return None
    return user


def create_user(session: Session, user_create: UserCreate) -> User:
    """
    Create a new user
    """
    # Check if user already exists
    statement = select(User).where(User.email == user_create.email)
    existing_user = session.exec(statement).first()
    if existing_user:
        raise error_response(
            error_code="RESOURCE_002",
            message="Email already registered",
            status_code=400
        )
    
    # Hash the password
    hashed_password = get_password_hash(user_create.password)
    
    # Create the user object
    db_user = User(
        email=user_create.email,
        password_hash=hashed_password
    )
    
    # Add to session and commit
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    
    return db_user


def login_user(session: Session, email: str, password: str):
    """
    Login a user and return JWT token
    """
    user = authenticate_user(session, email, password)
    if not user:
        raise error_response(
            error_code="AUTH_001",
            message="Invalid credentials",
            status_code=401
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=30)
    token_data = {
        "sub": str(user.id),
        "email": user.email
    }
    token = create_access_token(
        data=token_data, expires_delta=access_token_expires
    )
    
    return success_response(
        data={
            "user": UserRead(
                id=user.id,
                email=user.email,
                created_at=user.created_at,
                updated_at=user.updated_at
            ),
            "token": token
        },
        message="Login successful"
    )


def register_user(session: Session, user_create: UserCreate):
    """
    Register a new user and return JWT token
    """
    try:
        # Create the user
        db_user = create_user(session, user_create)
        
        # Create access token
        access_token_expires = timedelta(minutes=30)
        token_data = {
            "sub": str(db_user.id),
            "email": db_user.email
        }
        token = create_access_token(
            data=token_data, expires_delta=access_token_expires
        )
        
        # Return success response with user data and token
        return success_response(
            data={
                "user": UserRead(
                    id=db_user.id,
                    email=db_user.email,
                    created_at=db_user.created_at,
                    updated_at=db_user.updated_at
                ),
                "token": token
            },
            message="User registered successfully"
        )
    except Exception as e:
        # Handle error appropriately
        if hasattr(e, 'detail'):
            raise e
        raise error_response(
            error_code="VALIDATION_001",
            message=str(e),
            status_code=400
        )