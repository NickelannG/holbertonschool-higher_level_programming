#!/usr/bin/python3
"""
Takes in the name of a state as an argument and lists all cities of
that states in the hbtn_0e_4_usa database.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cur = db.cursor()
    state = sys.argv[4]
    query = "SELECT cities.name FROM cities " + \
        "INNER JOIN states ON cities.state_id = states.id " + \
            "WHERE BINARY states.name = %s " + \
            "ORDER BY cities.id ASC;"

    cur.execute(query, (state,))

    i = 0
    cities = cur.fetchall()
    for row in cities:
        i += 1
        if i < len(cities):
            print(row[0] + ", ", end="")
        else:
            print(row[0])
