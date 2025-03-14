import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer, ForeignKey("user.id"),primary_key=True)
    user_to_id = Column(Integer, ForeignKey("user.id"),primary_key=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    surname = Column(String(250), nullable=False)
    phone_number = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    inscriptionDate = Column(String(250), nullable=False)
    follower = relationship("follower")

class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    postal_code = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__= "post"
    id=Column(Integer, primary_key=True)
    created_date = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))

class Comment(Base):
    __tablename__= "comment"
    id = Column(Integer, primary_key=True)
    content = Column (String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Media(Base):
    __tablename__ = "media"
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
