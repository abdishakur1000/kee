from fastapi.testclient import TestClient
import pytest
from sqlalchemy import create_engine, engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from app.database import get_db, Base
from app.main import app
from alembic import command
from app.config import settings


# @pytest.fixture(scope='module')
@pytest.fixture()
def session():
    print('my session fixture ran')
    # drop all before we test
    Base.metadata.drop_all(bind=engine)
    # create new test database
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# @pytest.fixture(scope='module')
@pytest.fixture()
def client(session):
    # command.upgrade('head')# TODO WAA IN AAD SAMAYASAA ALEMBIC
    # command.downgrade('base')
    def override_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)



SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:agree101@localhost:5432/test_abdi'
# SQLALCHEMY_DATABASE_URL =\
#     f'postgresql://{settings.D_username}:' \
#     f'{settings.D_password}@{settings.D_hostname}:' \
#     f'{settings.D_port}/{settings.D_name}_test'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
