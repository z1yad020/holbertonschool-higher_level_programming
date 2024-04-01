#!/usr/bin/python3

"""
Contains `a`
"""

import sys

from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1],
             sys.argv[2],
             sys.argv[3]),
             pool_pre_ping=True)

    session = Session(engine)

    f = session.query(State).filter(State.name.ilike("%a%"))\
        .order_by(State.id).all()

    for r in f:
        print("{}: {}".format(r.id, r.name))
