#!/usr/bin/python3
"""
Script that connects  connects to a Mysql db and queries
"""


if __name__ == '__main__':
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[2],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         port=3306,
                         host='localhost')
    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE\
    '{:s}' ORDER BY id ASC".format(sys.argv[4]))

    for state in cur.fetchall():
        if state[1] == sys.argv[4]:
            print(state)

    cur.close()
    db.clode()
