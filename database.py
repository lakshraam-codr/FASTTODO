from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
import logging

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
	logging.warning("DATABASE_URL not set; falling back to sqlite:///./test.db")
	DATABASE_URL = "sqlite:///./test.db"

# For SQLite, need check_same_thread connect arg; for others, pass empty dict
connect_args = {"check_same_thread": False} if DATABASE_URL.startswith("sqlite") else {}
engine = create_engine(DATABASE_URL, connect_args=connect_args)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Import models to register them with Base
from models import Todo

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)