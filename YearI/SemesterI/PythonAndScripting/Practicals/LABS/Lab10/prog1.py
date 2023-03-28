from datetime import datetime
current_time = datetime.now()

print("LAB 10 Shubhang Gupta " + str(current_time))

blacklist = ['name1', 'name2', 'name3']
nostudent = int(input('Enter number of students: '))
studentlist = []
whitelist = []

for student in range(nostudent):
    prompt = input('Enter name of a student : ')
    while (prompt == ""):
        prompt = input('Enter a non-empty name of a student: ')
    studentlist.append(prompt)

for student in studentlist:
      if student not in blacklist:
            whitelist.append(student)

print('These ' + str(len(whitelist)) + ' students are allowed to give end sem.')
print(*sorted(whitelist), sep = "\n")

