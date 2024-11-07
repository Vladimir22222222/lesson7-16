# задание 1
s = str(input())
if s == s[::-1]:
  print("yes")
else:
  print("no")
# задание 2
mystring = str(input())
err=' '.join(mystring.split())
print(err)