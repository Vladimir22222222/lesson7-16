# задание №1 
n = int(input())
res = []
for i in range(n):
  a = int(input())
  res.append(a)
res.reverse()
print(res)
# задание №2
n = int(input())
s = list(map(int, input().split()))
m = s.pop(-1)
s.insert(0, m)
print(s)
# задание №3
m = int(input('Максимальная масса, которую может выдержать одна лодка: '))
n = int(input('Количество рыбаков: '))
weights = []
for _ in range(n):
    weights.append(int(input('вес рыбака: ')))
boats = 0
i = 0
j = n - 1
while i <= j:
  if i < j and weights[i] + weights[j] <= m:
      i += 1
  j -= 1
  boats += 1
print(boats)