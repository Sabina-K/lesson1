def ask_user(ans):
	try:
		while True:
			ans = input("Как дела? ")
			if ans == "Хорошо":
				print("Ну и отлично!")
				break
	except:
		print("Нужен аргумент")
ask_user()


