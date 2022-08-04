#!/usr/bin/python3
"""Module to  lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY id ASC')
    data = cursor.fetchall()
    for item in data:
        print(item)

    db.close()
