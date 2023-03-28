import datetime
current_time = datetime.datetime.now()
print("LAB 12 SHUBHANG GUPTA",str(current_time))

import pandas as pd
import sqlite3
df= pd.DataFrame({'name':['juan', 'victoria','mary'],
                 'age': [23,24,25],
                 'city': ['miami', 'buenos aires','santiago']})

con = sqlite3.connect('DFIS_sql.db')
df.to_sql('friends', con)

c=con.cursor()

c.execute('SELECT * FROM friends')
print(c.fetchall())

c.close()
con.close()

