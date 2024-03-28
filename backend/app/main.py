from fastapi import FastAPI, Depends
from fastapi_users import FastAPIUsers

from app.base_config import auth_backend
from app.manager import get_user_manager
from app.schemas import UserRead, UserCreate
from app.models import User

app = FastAPI(
    title="Title"
)

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)



current_user = fastapi_users.current_user()
