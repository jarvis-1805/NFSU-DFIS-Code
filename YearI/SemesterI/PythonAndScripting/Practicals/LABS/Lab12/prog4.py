import datetime
current_time = datetime.datetime.now()
print("LAB 12 SHUBHANG GUPTA",str(current_time))

import pandas as pd
import sqlite3
df1 = pd.read_excel('book.xlsx')

con = sqlite3.connect('db2.db')
df1.to_sql('students', con)

c=con.cursor()

c.execute('SELECT * FROM students')
print(c.fetchall())

