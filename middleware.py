from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
import os
from dotenv import load_dotenv
from models import User

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

if SECRET_KEY is None:
    raise ValueError("La clé secrète (SECRET_KEY) est manquante dans le fichier .env")

def get_user_from_token(authorization: str) -> User:
    if not authorization:
        raise HTTPException(status_code=401, detail="Authorization token missing")

    try:
        token = authorization.split("Bearer ")[1]
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        user_email = payload.get("email")
        user_id = payload.get("sub")

        print("eeeee", type(user_id))

        if not user_email or not user_id:
            raise HTTPException(status_code=401, detail="Invalid token")
        
        return User(id=int(user_id), email=user_email)

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")


class AddUserToContext(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        authorization = request.headers.get("Authorization")
        if authorization:
            user = get_user_from_token(authorization)
            request.state.user = user
        else:
            request.state.user = None

        response = await call_next(request)
        return response
