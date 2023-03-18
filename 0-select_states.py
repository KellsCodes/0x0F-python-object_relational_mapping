#!/usr/bin/python3
'''import required modules'''

import MySQLdb
import sys

'''
    Command line arguments for for mysql username,
    mysql password, and database name
'''
_args = sys.argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=_args[1],
            passwd=_args[2], db=_args[3], charset='utf8', port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()

