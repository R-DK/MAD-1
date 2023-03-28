from application.database import db 
from main import app 

def test_no_articles_home():
    # STEP 1 : Arranging
    client = app.test_client()
    ctx = app.app_context()
    ctx.push()
    db.create_all()

    # STEP 2 : Acting
    response = client.get("/")

    # STEP 3 : Asserting
    assert b"<title>All Articles</title>" in response.data

    # STEP 4 : Cleaning
    ctx.pop()
    db.drop_all()