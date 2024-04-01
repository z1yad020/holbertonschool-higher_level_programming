#!/usr/bin/python3

"""
First state model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()


class State(Base):
    """state table"""
    __tablename__ = 'states'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                autoincrement=True)

    name = Column(String(128), nullable=False)
