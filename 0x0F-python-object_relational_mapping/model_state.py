#!/usr/bin/python3
"""Module contains the class definition of a State and an Instance
 Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """The class States"""
    __tablename__ = 'states'
    id = Column(Integer,  nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(128), nullable=False)
