#!/usr/bin/python3

"""
First state
"""

import sqlalchemy
import sys
from model_state import State, Base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1],
             sys.argv[2],
             sys.argv[3]),
             pool_pre_ping=True)

    Session = sessionmaker(bind=engine)

    session = Session()

    Base.metadata.create_all(engine)

    f = session.query(State).first()

    if f is not None:
        print("{}. {}".format(f.id, f.name))
    else:
        print("Nothing")
