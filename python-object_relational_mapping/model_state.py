#!/usr/bin/python3
"""
This module contains the State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """This class defines a state"""
    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column("name", String(128), nullable=False)
