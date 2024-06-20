#!/usr/bin/python3
""" Lists all values in the states table in the hbtn_0e_0_usa database
where name matches the argument and is safe from MySQL injections
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    cur = db.cursor()
    state = sys.argv[4]
    query = "SELECT * FROM states WHERE BINARY name = %s"
    "ORDER BY states.id ASC"
    cur.execute(query, (state,))
    for row in cur.fetchall():
        print(row)
