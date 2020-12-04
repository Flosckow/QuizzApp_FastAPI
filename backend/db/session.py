from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
import databases
from backend.core import config

# engine = create_engine(config.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
# db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
engine = create_engine(config.SQLALCHEMY_DATABASE_URI, connect_args={"check_same_thread": False})
database = databases.Database(config.SQLALCHEMY_DATABASE_URI)
Base: DeclarativeMeta = declarative_base()
