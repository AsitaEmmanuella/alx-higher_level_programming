#!/usr/bin/python3
"""
This module defines the State class and sets up the SQLAlchemy connection.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Create a base class for database models
Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): The unique identifier for the state.
        name (str): The name of the state.
    """

    __tablename__ = "states"

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"State(id={self.id}, name='{self.name}')"
