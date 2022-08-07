#!/usr/bin/python3
"""Module to list all cities
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states INNER JOIN cities ON states.id=cities.state_id\
    WHERE states.name LIKE %s ORDER BY cities.id ASC"

    cursor.execute(sql, (sys.argv[4], ))
    data = cursor.fetchall()
    i = 0
    for i in range(len(data)):
        print(str(data[i][4]), end='')
        if i != (len(data) - 1):
            print(", ", end='')
    print()
    db.close()
