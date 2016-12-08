names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person(name):
	for n in names:
		name = input("Введите имя: ")
		if name == n:
			print("Имя есть в списке")
		else:
			print("Вас нет в списке")
find_person("Kate")

  	