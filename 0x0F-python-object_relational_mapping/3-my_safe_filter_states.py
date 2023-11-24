#!ussr/bin/python3
"""
Querry using MySQLdb
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(username=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         host="localhost",
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE\
    %(state_name)s ORDER BY id ASC", {'state_name': sys.argv[4]})
    for state in cur.fetchall():
        if state[1] == sys.argv[4]:
            print(state)
    db.close()
