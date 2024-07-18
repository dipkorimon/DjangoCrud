from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from django.conf import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URL)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Book(Base):
  __tablename__ = 'myapp_book'
  id = Column(Integer, primary_key=True)
  title = Column(String)
  author = Column(String)
  published_date = Column(Date)
  isbn = Column(String)

  def __repr__(self):
    return f"<Book(title={self.title}, author={self.author}, published_date={self.published_date}, isbn={self.isbn})>"
