#!/usr/bin/python3
"""Module print of database names start with N
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])

    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%'"
    cursor.execute(sql)
    data = cursor.fetchall()
    for item in data:
        if item[1][0] == 'N':
            print(item)

    db.close()
