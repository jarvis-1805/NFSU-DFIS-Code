import datetime
current_time = datetime.datetime.now()
print("LAB 12 SHUBHANG GUPTA",str(current_time))

import sqlite3

conn=sqlite3.connect('datab11.db')
print("Conected to the database")
c=conn.cursor()

c.execute("""CREATE TABLE student (ID integer,
Name text,
Phone integer
)""")

c.execute("INSERT INTO student VALUES (3,'kunit',5555574321)")
c.execute("INSERT INTO student VALUES (4,'junit',5555098755)")
c.execute("INSERT INTO student VALUES (5,'sunit',9999974321)")
print("Total number of rows updated :",conn.total_changes)

c.execute("SELECT * FROM student")
print(c.fetchall())

conn.execute("UPDATE student SET Name = 'Saam' where ID=3")
c.execute("DELETE from student where Name='Saam'")

rows = c.execute("SELECT * FROM student")
for i in rows:
  print(i)

c.close()
conn.close()

