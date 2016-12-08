dialog = {"привет": "и тебе привет!", "как дела": "лучше всех"}
def get_answer(key,chat):
	return chat[key.lower()]
	key = input()
	 
get_answer("Привет", dialog)
from ask_user.py import ask_user
ask_user("Пока")



