from fastapi import Request, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
from jwt import PyJWTError
from typing import Dict, Optional
import os
from dotenv import load_dotenv

load_dotenv()

# Secret key for JWT signing
SECRET_KEY = os.getenv("SECRET_KEY", "your-super-secret-jwt-signing-key-change-in-production")
ALGORITHM = "HS256"

security = HTTPBearer()


def decode_access_token(token: str) -> Optional[Dict]:
    """
    Decode and verify the JWT token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except PyJWTError:
        return None


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    Get the current user from the JWT token
    """
    token = credentials.credentials
    user_data = decode_access_token(token)
    
    if user_data is None:
        raise HTTPException(
            status_code=401,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Check if token has expired
    # Note: In a real application, you would also check the 'exp' claim
    
    return user_data