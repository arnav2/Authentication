import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy import Column, String, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from datetime import datetime
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'USER'

    id = Column(String, primary_key=True)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(DateTime, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)

    def __init__(self, email, password, created_at = datetime.now(), is_active = True):
        self.id = uuid.uuid1().__str__()
        self.email = email
        self.password = password
        self.created_at = created_at
        self.is_active = is_active
    
    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email}, created_at={self.created_at}, is_active={self.is_active})>"

class Database:
    def __init__(self, stage="ALPHA"):
        # Load environment variables from .env file
        load_dotenv()
        # Database configuration
        self.DB_HOST = os.getenv(stage + '_DB_HOST')
        self.DB_PORT = os.getenv(stage + '_DB_PORT')
        self.DB_NAME = os.getenv(stage + '_DB_NAME')
        self.DB_USER = os.getenv(stage + '_DB_USER')
        self.DB_PASSWORD = os.getenv(stage + '_DB_PASSWORD')

        self.DB_URL = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

        self.engine = create_engine(self.DB_URL, pool_size=10, max_overflow=100, pool_timeout=10)
    
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def __repr__(self):
        return self.DB_URL
