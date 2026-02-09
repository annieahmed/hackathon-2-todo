from fastapi import APIRouter, Depends, HTTPException, status, Form
from sqlmodel import Session
from ..database import get_session
from ..models.user import UserCreate, UserRead
from ..services.auth_service import register_user, login_user
from ..middleware.jwt_middleware import get_current_user
from ..utils.responses import success_response, error_response


router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register", response_model=UserRead)
def register(
    email: str = Form(...),
    password: str = Form(...)
):
    """
    Register a new user
    """
    # Create UserCreate object from form data
    user_create = UserCreate(email=email, password=password)
    
    # Since we need a session, we'll create a temporary function that gets the session
    # In a real implementation, this would be handled differently
    from sqlmodel import create_engine
    from sqlalchemy.orm import sessionmaker
    from ..config.database import DATABASE_URL
    
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    with SessionLocal() as session:
        return register_user(session, user_create)


@router.post("/login")
def login(
    email: str = Form(...),
    password: str = Form(...)
):
    """
    Authenticate user and return JWT token
    """
    from sqlmodel import create_engine
    from sqlalchemy.orm import sessionmaker
    from ..config.database import DATABASE_URL
    
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    with SessionLocal() as session:
        return login_user(session, email, password)


@router.post("/logout")
def logout(current_user: dict = Depends(get_current_user)):
    """
    Logout user (invalidate session)
    """
    # In a JWT-based system, the logout is typically handled on the client side
    # by removing the token from storage. For server-side invalidation,
    # you would need to implement a token blacklist mechanism.
    return success_response(message="Logged out successfully")


@router.get("/me", response_model=UserRead)
def get_current_user_info(current_user: dict = Depends(get_current_user)):
    """
    Get current user information from JWT token
    """
    # In a real implementation, we would fetch the user from the database
    # using the user ID from the token
    return success_response(
        data={
            "user": {
                "id": current_user.get("sub"),
                "email": current_user.get("email"),
                "created_at": "2023-01-01T00:00:00Z",  # Placeholder
                "updated_at": "2023-01-01T00:00:00Z"  # Placeholder
            }
        },
        message="User information retrieved successfully"
    )