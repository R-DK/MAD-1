def test_no_articles_home(client, init_database):

    print('RUNNING')

    # STEP 2 : Acting
    response = client.get("/")

    # STEP 3 : Asserting
    assert b"<title>All Articles</title>" in response.data
