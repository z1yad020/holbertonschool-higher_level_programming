#!/usr/bin/python3

'''
All states via SQLAlchemy
'''

from model_state import State, Base
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session
import MySQLdb
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1],
             sys.argv[2],
             sys.argv[3]),
             pool_pre_ping=True)

    Session = Session(engine)

    Base.metadata.create_all(engine)


    states = Session.query(State).all()


    for row in states:
        print("{}: {}".format(row.id, row.name))
