#!/usr/bin/python3
"""
Querry using MySQLdb
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)
    cursor = db.cursor()

    query = f"""
    SELECT GROUP_CONCAT(cities.name SEPARATOR ', ')
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name = '{state_name}'
    ORDER BY cities.id;
    """

    cursor.execute(query)

    result = cursor.fetchone()

    if result and result[0]:
        print(result[0])

    cursor.close()
    db.close()
