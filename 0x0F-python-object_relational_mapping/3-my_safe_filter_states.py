#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the provided argument, and is safe from SQL injection.
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

    # Execute the SQL query to fetch states with the provided name
    m = sys.argv[4]
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id", (m, )
    )

    # Fetch and print the results
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
