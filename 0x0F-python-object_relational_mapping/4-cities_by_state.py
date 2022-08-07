#!/usr/bin/python3
"""Module to list all cities
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states INNER JOIN cities ON states.id=cities.state_id\
    ORDER BY cities.id ASC"

    cursor.execute(sql)
    data = cursor.fetchall()
    for row in data:
        print("(" + str(row[2]) + ", '" + str(row[4]) +
              "', '" + str(row[1]) + "')")
    db.close()
