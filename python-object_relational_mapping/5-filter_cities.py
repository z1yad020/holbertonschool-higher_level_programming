#!/usr/bin/python3

'''
All cities by state
'''

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)

    cur = db.cursor()

    cur.execute("SELECT cities.name FROM cities \
                 JOIN states ON  cities.state_id = states.id \
                 WHERE BINARY states.name = %s \
                 ORDER BY cities.id", (sys.argv[4],))

    rows = cur.fetchall()
    if rows is not None:
        print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()
