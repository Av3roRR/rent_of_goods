from app.exceptions import TokenAbsentException
from fastapi import Request

def get_token(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        raise TokenAbsentException
    return token