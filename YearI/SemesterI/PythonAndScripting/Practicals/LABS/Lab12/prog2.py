import datetime
current_time = datetime.datetime.now()
print("LAB 12 SHUBHANG GUPTA",str(current_time))

conn=sqlite3.connect('datab1.db')
print("Conected to the database")
c=conn.cursor()

c.execute("CREATE TABLE person (name, age, id)")

n=3
print ("Enter 3 students names:")
name = [input() for i in range(n)]
print ("Enter 3 students age:")
age = [int(input()) for i in range(n)]
print ("Enter 3 students ids:")
id = [int(input()) for i in range(n)]
m = len(name)
for i in range(m):
  c.execute("insert into person values(?,?,?)", (name[i], age[i], id[i]))

c.execute("SELECT * FROM person")
print(c.fetchall())

c.close()
conn.close()

