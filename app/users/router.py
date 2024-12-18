

from fastapi import APIRouter, Response

from app.database import async_session_maker
from app.users.schemas import UserResponse, UserCreate, UserLogin, TokenResponse
from app.users.services import register_user_service, login_user_service

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

@router.post("/register",response_model=UserResponse)
async def register_user(user:UserCreate):
    async with async_session_maker() as session:
        return await register_user_service(user,session)


@router.post("/login",response_model=TokenResponse)
async def login(response: Response,user:UserLogin):
    async with async_session_maker() as session:
        return await login_user_service(response,user,session)


@router.post("/logout", response_model= bool)
async def logout(response : Response):
    #async with async_session_maker() as session:
    response.delete_cookie("access_token",httponly=True)
    return True