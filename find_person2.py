names = ["Вася", "Маша", "Петя", "Валера", "Саша", "Даша"]
def find_person(n):
	for n in names:
		if n == "Валера":
			print("Валера нашелся")
		else: 
			print(n)

find_person("Даша")