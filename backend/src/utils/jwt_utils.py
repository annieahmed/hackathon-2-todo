from datetime import datetime, timedelta
from typing import Optional
import jwt
from jwt import PyJWTError
import os


# Secret key for JWT signing
SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-jwt-signing-key-change-in-production")
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10080  # 7 days in minutes


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """
    Create a JWT access token
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str) -> Optional[dict]:
    """
    Decode and verify the JWT token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None


def get_current_user_from_token(token: str) -> Optional[dict]:
    """
    Get the current user from the JWT token
    """
    payload = decode_access_token(token)
    
    if payload is None:
        return None
    
    # Check if token has expired
    # Note: In a real application, you would also check the 'exp' claim
    
    return payload