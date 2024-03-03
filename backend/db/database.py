import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

class Database:
    def __init__(self):
        # Load environment variables from .env file
        load_dotenv()
        # Database configuration
        self.DB_HOST = os.getenv('DB_HOST')
        self.DB_PORT = os.getenv('DB_PORT')
        self.DB_NAME = os.getenv('DB_NAME')
        self.DB_USER = os.getenv('DB_USER')
        self.DB_PASSWORD = os.getenv('DB_PASSWORD')

        self.DB_URL = f"postgresql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        self.engine = create_engine(self.DB_URL)
    
    def __repr__(self):
        return self.DB_URL
    
    
    