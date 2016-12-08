def ask_user(ans):
	while True:
		ans = input("Как дела? ")
		if ans == "Хорошо":
			print("Ну и отлично!")
			break
		
print(ask_user("что написать тут?"))
