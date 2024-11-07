#решение задание №1
n = int(input("Введите количество элементов списка "))
s = list(map(int, input().split()))
e = set(s)
print(len(e))

# решение задание №2
a = set(input().split())
b = set(input().split())
print (len(a.intersection(b)))

# решение задание №3
a = set()
for i in input().split():
    if i not in a:
        a.add(i)
        print('NO')
    else:
        print('YES')