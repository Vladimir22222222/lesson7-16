#задание №1
pets_dict1 = {}
pets_dict2 = {}
while (True):
	k = input("Введите имя питомца  (клавиша enter - выход): ")
	if k == '':
		break
	else:
		k1 = input('Вид питомца: ')
		k2 = int(input('Возраст питомца: '))
		k3 = input('Имя владельца:  ')
		pets2 = {'Вид питомца:':k1, 'Возраст питомца:':k2, 'Имя владельца:':k3}
		break
pets_dict1[k] = pets_dict2
for key, value in pets_dict1.items():
		vid = value['Вид питомца:']
		age = value['Возраст питомца:']
		imy = value['Имя владельца:']
		year_case = ''
if age % 10 == 1 and age != 11 and age % 100 != 11:
		year_case = 'год'
elif 1 < age % 10 <= 4 and age != 12 and age != 13 and age != 14:
		year_case = 'года'
else:
		year_case = 'лет'
print("Это", vid, "по кличке", key,". Возраст питомца:", age, year_case, "Имя владельца:", imy)

#задание №2
my_dict = {}
for i in range(10, -6,-1):
	my_dict[i] = i ** i
print(my_dict)