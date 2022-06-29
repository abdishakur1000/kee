from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings
import psycopg2
import time


SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.D_username}:" \
    f"{settings.D_password}@{settings.D_hostname}:{settings.D_port}/{settings.D_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='abdi', user='postgres',
#                                 password='agree101', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database Connection was successful....')
#         break
#     except Exception as error:
#         print('Connection Failed.!!!!!')
#         print('Error', error)
#         time.sleep(3)


# my_posts = [{"title": "title of post 1", "content": "content of post 1", "id": 1}, {
#     "title": "favorite food", "content": "I like pizza", "id": 2}]
#
#
# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
#
#
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i
#
#
