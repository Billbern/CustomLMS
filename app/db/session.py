import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sesssionmaker

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

engine = create_engine(
    SQLALCHEMY_DATABASE_URI,
    connect_args={"check_same_thread": False},
)

SessionLocal = sesssionmaker(autocommit=False, autoflush=False, bind=engine)
