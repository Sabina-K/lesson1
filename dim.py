names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
name = input("Введите имя: ")
for n in names:
	if name == n:
		print("Имя есть в списке")
	else:
		print("Вас нет в списке")



names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
x = input("Введите имя: ")
def find_person(name):	
	for n in names:
		if name == n:
			print("Имя есть в списке")
		else:
			print("Вас нет в списке")
find_person(x)
