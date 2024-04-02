#!/usr/bin/python3

"""
First city model
"""


from sqlalchemy import Column, Integer, String, ForeignKey

from model_state import Base


class City(Base):
    """cities table"""
    __tablename__ = 'cities'

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False,
                autoincrement=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
