from typing import Any, Dict, Optional
from fastapi import HTTPException


def create_response(success: bool, data: Any = None, message: str = "", error: Optional[Dict] = None) -> Dict:
    """
    Create a standardized response
    """
    response = {
        "success": success,
        "message": message
    }
    
    if data is not None:
        response["data"] = data
    
    if error is not None:
        response["error"] = error
    
    return response


def success_response(data: Any = None, message: str = "") -> Dict:
    """
    Create a success response
    """
    return create_response(success=True, data=data, message=message)


def error_response(error_code: str = "", message: str = "", status_code: int = 400) -> HTTPException:
    """
    Create an error response
    """
    error = {
        "code": error_code,
        "message": message
    }
    response = create_response(success=False, error=error)
    return HTTPException(status_code=status_code, detail=response)