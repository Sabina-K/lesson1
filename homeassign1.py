age = int(input("Введите ваш возраст: "))
if age > 4 and age < 7:
	print("Вам в детский сад")
elif age >= 7 and age < 18:
	print("Вам в школу")
elif age >18 and  age < 24:
	print("Универ")
elif age >= 24:
	print("Пора работать")