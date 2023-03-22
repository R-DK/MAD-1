from flask import Flask, request, render_template
from flask import current_app as app
from models import Article

@app.route("/", methods=["GET", "POST"])
def articles():
    if request.method == "GET":
        #articles = db.session.query(Article).all()
        articles = Article.query.all()
        return render_template("articles.html", articles=articles)

@app.route("/articles_by/<username>", methods=["GET", "POST"])
def articles_by_author(username):
    if request.method == "GET":        
        articles = Article.query.filter(Article.authors.any(username=username))
        return render_template("articles_by_author.html", articles=articles)