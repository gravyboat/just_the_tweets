#!/usr/bin/python3

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
Session = sessionmaker()

class TwitterUser(Base):

    __tablename__ = 'twitter_users'

    id = Column(Integer, primary_key = True)
    name = Column(String)
    username = Column(String)
    password = Column(String)
    email = Column(String)



    def __init__(self, name, username, password, email):
        self.name = name
        self.username = username
        self.password = password
        self.email = email

