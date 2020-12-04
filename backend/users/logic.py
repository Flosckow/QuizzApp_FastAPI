from fastapi_users.authentication import JWTAuthentication
from fastapi_users.db import SQLAlchemyUserDatabase
from .models import UserTable
from .schemas import UserDB
from ..db.session import database

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)



SECRET = "dsadasdwq314r3rferghu678"

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET, lifetime_seconds=3600)

auth_backends.append(jwt_authentication)