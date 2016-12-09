dialog = {"привет": "и тебе привет!", "как дела": "лучше всех"}
def get_answer(key,chat):
	return chat[key]
	key = input()
	 
get_answer("Привет", dialog)
from ask_user.py import ask_user
ask_user("Пока")



dialog = {"привет": "и тебе привет!", "как дела?": "лучше всех!", "пока":"увидимся", "Что делаешь?":"Смотрю кино", "Какой фильм":"Молчание ягнят"}
while True:
	def get_answer(key, chat):
		return chat[key.lower()]
	key = input()
	print(get_answer(key, dialog))
if 


def ask_user(ans):
	while True:
		ans = input("Как дела? ")
		if ans == "Хорошо":
			print("Ну и отлично!")
			break
		
print(ask_user("что написать тут?"))
