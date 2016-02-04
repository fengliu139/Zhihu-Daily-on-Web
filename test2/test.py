import sqlite3
import os
import datetime
#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
sqlite_file = os.path.join(BASE_DIR, 'main.db')
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (1, 'test')".format(tn='dateinfo', idf='id', cn='data'))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format('id'))
conn.commit()
conn.close()
'''

s='20120601'
date=s
print datetime.date(int(date[0:4]),int(date[4:6]),int(date[6:8]))
