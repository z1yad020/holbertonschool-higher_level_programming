#!/usr/bin/python3

"""
Cities in state
"""

import sys

from model_state import Base, State
from model_city import City

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == '__main__':

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
             sys.argv[1],
             sys.argv[2],
             sys.argv[3]),
             pool_pre_ping=True)

    session = Session(engine)

    rows = session.query(State, City).filter(State.id == City.state_id)\
            .order_by(City.id).all()

    for s, c in rows:
        print("{}: ({}) {}".format(s.name, c.id, c.name))
