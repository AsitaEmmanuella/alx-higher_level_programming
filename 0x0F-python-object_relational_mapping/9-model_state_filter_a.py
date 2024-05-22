#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a'
from the hbtn_0e_6_usa database.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

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

    # Fetch and print all State objects containing the letter 'a'
    for state in session.query(State).filter(State.name.like("%a%")):
        print(state.id, state.name, sep=": ")

    # Close the session
    session.close()
