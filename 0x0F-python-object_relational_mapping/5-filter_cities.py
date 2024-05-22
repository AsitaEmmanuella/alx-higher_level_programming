#!/usr/bin/python3

"""
This script lists all cities of a given state from the hbtn_0e_4_usa database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get the command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

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

    # Execute the SQL query to fetch cities of the given state
    cursor.execute(
        """SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""",
        (sys.argv[4],),
    )

    # Fetch and print the results
    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")

    # Close the cursor and the database connection
    cursor.close()
    db.close()
