#!/usr/bin/python3
"""Module to Find state (only one)
"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()

    sql = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    cursor.execute(sql, (sys.argv[4],))
    data = cursor.fetchall()
    for item in data:
        print(item)
    db.close()
