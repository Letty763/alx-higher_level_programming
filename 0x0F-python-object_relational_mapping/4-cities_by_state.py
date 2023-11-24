#!/usr/bin/python3
'''
fetch cities from db
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         password=argv[2],
                         database=argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name\
    FROM cities INNER JOIN states ON cities.state_id = states.id ORDER BY\
    cities.id ASC")

    for row in cursor.fetchall():
        print(row)
    db.close()
