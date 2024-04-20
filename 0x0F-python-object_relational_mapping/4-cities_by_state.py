#!/usr/bin/python3

"""
This script lists all cities from the hbtn_0e_4_usa database.
"""


import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=database_name,
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query to fetch all cities
    cursor.execute(
        """SELECT cities.id, cities.name, states.name FROM
                cities INNER JOIN states ON states.id=cities.state_id"""
    )

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
