dialog = {"привет": "и тебе привет!", "как дела?": "лучше всех!", "пока":"увидимся"}
while True:
	def get_answer(key, chat):
		return chat[key.lower()]
	key = input()
	print(get_answer(key, dialog))




