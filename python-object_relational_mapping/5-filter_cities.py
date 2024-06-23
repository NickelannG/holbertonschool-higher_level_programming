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
    query = "SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ') " + \
            "FROM cities " + \
            "INNER JOIN states ON cities.state_id = states.id " + \
            "WHERE BINARY states.name = %s;"

    cur.execute(query, (state,))

    #i = 0
    #cities = cur.fetchall()
    #for row in cities:
    #    print("{}".format(row[1]), end="")
    #    i += 1
    #    if i != len(cities):
    #        print(", ", end="")
    #print("")

    for row in cur.fetchall():
        print(row[0])