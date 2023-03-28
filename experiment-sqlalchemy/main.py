import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy import Table_Column, Integer, String, ForeignKey
from sqlalchemy import select

from sqlalchemy.orm import Session, declarative_base, relationship

Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	user_id = Column(Integer, autoincrement=True, primary_key=True)
	username = Column(String, unique=True)
	email = Column(String, unique = True)
	
class Article(Base):
	__tablename__ = 'article'
	article_id = Column(Integer, primary_key=True, autoincrement=True)
	title = Column(String)
	content = Column(String)
	authors = relationship("User", secondary="article_authors")
	
class ArticleAuthors(Base):
	__tablename__ = 'article_authors'
	user_id = Column(Integer, ForeignKey("user.user_id"), primary_key = True, nullable=False)
	article_id = Column(Integer, ForeignKey("article.article_id"), primary_key=True, nullable=False)
