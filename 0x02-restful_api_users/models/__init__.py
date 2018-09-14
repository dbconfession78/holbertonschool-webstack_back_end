#!/usr/bin/python3
from models.base_model import Base
from models.user import User
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

user = os.getenv("HBNB_YELP_MYSQL_USER")
pw = os.getenv("HBNB_YELP_MYSQL_PWD")
host = os.getenv("HBNB_YELP_MYSQL_HOST")
db = os.getenv("HBNB_YELP_MYSQL_DB")
db_engine = None

if db:
    db_engine = create_engine('mysql+pymysql://{}:{}@{}/{}'.format(user, pw,
                                                                   host, db))
if os.getenv("HBNB_YELP_ENV") == "test":
    Base.metadata.drop_all(db_engine)

if db_engine:
    Base.metadata.create_all(db_engine)
    db_session = scoped_session(sessionmaker(bind=db_engine,
                                             expire_on_commit=False))
