import random
m = int(input('m = '))
n = int(input('n = '))
matrix_1 = [[random.randint(1, 11) for j in range(n)] for i in range(m)]
print('Matrix 1: ')
for i in range(m):
	print(matrix_1[i])
matrix_2 = [[random.randint(1, 11) for j in range(n)] for i in range(m)]
print('Matrix 2: ')
for i in range(m):
	print(matrix_2[i])
result = [[matrix_1[i][j] + matrix_2[i][j]  for j in range
(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Результат сложения двух матриц: ")
for r in result:
	print(r)