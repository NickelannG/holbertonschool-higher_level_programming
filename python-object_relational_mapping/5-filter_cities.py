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
    
    for av in sys.argv:
        if av.count(";") > 0:
            exit()

    cur = db.cursor()
    state = sys.argv[4]
    query = "SELECT GROUP_CONCAT(name ORDER BY name ASC SEPARATOR ', ') " + \
            "FROM (" + \
            "SELECT cities.name FROM cities " +\
            "LEFT JOIN states ON cities.state_id = states.id " + \
            "WHERE BINARY states.name = %s " + \
            ") AS city_names;"

    cur.execute(query, (state,))

    for row in cur.fetchall():
        print(row[0])
