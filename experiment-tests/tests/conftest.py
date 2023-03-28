import pytest
from main import app
from application.database import db

@pytest.fixture(scope="module")
def client():
    print('SETTING UP CLIENT')
    # STEP 1 : Arranging
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()

    yield client 

    # STEP 4 : Cleaning
    print('CLEANING UP CLIENT')
    ctx.pop()

@pytest.fixture(scope="module")
def init_database():
    print('SETTING UP DB')
    # STEP 1 : Arranging
    db.create_all()

    yield db 

    # STEP 4 : Cleaning
    print('CLEANING UP DB')
    db.drop_all()
