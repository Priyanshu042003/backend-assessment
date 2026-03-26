from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
import time

DATABASE_URL = os.getenv("DATABASE_URL")

for i in range(3):
    try:
        engine = create_engine(DATABASE_URL)
        engine.connect()
        print("Database connected")
        break
    except Exception as e:
        print("Waiting for DB...", e)
        time.sleep(3)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()