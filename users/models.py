from sqlalchemy.orm import relationship
from db.base_class import Base
from sqlalchemy import Column, String, Integer, Boolean


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=False)
    is_superuser = Column(Boolean, default=False)

    # poll = relationship("Poll", back_populates="user")
    # survey = relationship("Survey", back_populates="user")
    # answer = relationship("Answer", back_populates="user")




