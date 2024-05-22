#!/usr/bin/python3
"""
This script lists all State objects from the hbtn_0e_6_usa database.
"""
import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

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


if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database_name}"
    )

    # Create a session
    session = Session(engine)

    # Fetch and print all State objects
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
