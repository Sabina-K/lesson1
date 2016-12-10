dialog = {"привет": "и тебе привет!", "как дела": "лучше всех", "пока":"увидимся"}
def get_answer(key, chat):
	return chat[key.lower()]
key = input()
print(get_answer("привет", dialog))

#При помощи функции get_answer()
# отвечать на вопросы пользователя в ask_user(), пока он не скажет “Пока!”

def ask_user(ans):
	while True:
		ans = input("Как дела? ")
		if ans == "Хорошо":
			print("Ну и отлично!")
			break
ask_user("Как дела?")


while True:
		ans = input("Как дела? ")
		if ans == "Хорошо":
			print("Ну и отлично!")
			break
		
ask_user(" ")

