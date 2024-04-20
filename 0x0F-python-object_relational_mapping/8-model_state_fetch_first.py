#!/usr/bin/python3
"""
This script prints the first State object from the hbtn_0e_6_usa database.
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

    # Fetch the first State object
    first_state = session.query(State).first()

    # Print the result
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close the session
    session.close()
