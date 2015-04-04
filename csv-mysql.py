#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import csv
import traceback
import sys
import MySQLdb

try:

    mysql_db = MySQLdb.connect(host='hostname', user='username', 
        passwd='password', db='databasename')
    c = mysql_db.cursor()

    csv_data = csv.reader(file('output_data.csv'))

    for row in csv_data:
        # Use as many "%s" as you have fields, separated by commas
        query = '''INSERT INTO tablename(allfieldnames)VALUES(%s)'''
        c.execute(query, (row))

    mysql_db.commit()

except Exception:
    print(traceback.print_exc())
    c.close()
    sys.exit(2)
else:
    print('MySQL database updated successfully!')
finally:
    c.close()
    sys.exit()
