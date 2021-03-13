from sqlalchemy.orm import relationship

from backend.db.session import Base
from sqlalchemy import Column, String, Integer, Boolean, DateTime

from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase


class UserTable(Base, SQLAlchemyBaseUserTable):
    name = Column(String, unique=True)
    date = Column(DateTime)
    poll = relationship("Poll", back_populates="user")
    survey = relationship("Survey", back_populates="user")


users = UserTable.__table__

# class User(Base):
#     id = Column(Integer, primary_key=True, index=True)
#     full_name = Column(String, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=False)
#     is_superuser = Column(Boolean, default=False)
#
# #     # poll = relationship("Poll", back_populates="user")
# #     # survey = relationship("Survey", back_populates="user")

