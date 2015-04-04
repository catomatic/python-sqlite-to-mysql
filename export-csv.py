#!/usr/bin/python

# author: catomatic
# website: https://github.com/catomatic
# source: personal projects library

import csv
import traceback
import sys
import sqlite3

try:

    sqlite_db = 'databasename'
    conn = sqlite3.connect(sqlite_db)
    c = conn.cursor()

    query = '''SELECT allfieldnames FROM tablename'''

    c.execute(query)

    rows = list(c.fetchall())

    data_list = [list(i) for i in rows]

    with open('output_data.csv', 'w') as csv_file:
        output = csv.writer(csv_file, delimiter=',')
        output.writerows(data_list)

except Exception:
    print(traceback.print_exc())
    conn.close()
    sys.exit(2)
else:
    print('Data converted to csv successfully!')
finally:
    conn.close()
    sys.exit()
