#!/usr/bin/python3
""" Lists all states from the hbtn_0e_0_usa database"""
import MySQLdb
import sys

db = MySQLdb.connect(
    host="localhost",
    port=3306,
    user=sys.argv[1],
    passwd=sys.argv[2],
    db=sys.argv[3]
)
cur = db.cursor()
cur.execute("SELECT * FROM states ORDER BY states.id ASC")
for row in cur.fetchall():
    print(row)
