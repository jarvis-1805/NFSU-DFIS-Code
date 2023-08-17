x1 = [44, 33, 31, 40, 50, 69]
x2 = [44, 100, 300, 70, 120, 200]
x3 = [1, 0, 1, 1, 0, 1]
x4 = ['No', 'Yes', 'Yes', 'No', 'No', 'Yes']
dist = list()
norm = list()
min = min(x1)
max = max(x1)

for i in range(0, 6):
  temp1 = (x1[i] - 73) ** 2
  temp2 = (x2[i] - 125) ** 2
  temp3 = (x3[i] - 0) ** 2
  dist.append((temp1 + temp2 + temp3) ** 0.5)
  norm.append((x1[i] - min) / (max - min))

print('Age', 'Salary', 'Credit_Score', 'Get_loan', 'Distance', '                 Norm', '                    Std.')  
for i in range(0, 6):
  print(x1[i], end='   ')
  print(x2[i], end='      ')
  if x3[i] == 1: print('High', end='         ')
  else: print('Low', end='         ')
  print(x4[i], end='      ')
  print(dist[i], end='        ')
  print(norm[i])

