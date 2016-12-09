dialog = {"привет": "и тебе привет!", "как дела?": "лучше всех!", "что делаешь?":"смотрю кино", "какой фильм":"молчание ягнят"}
while True:
	def get_answer(key, chat):
		return chat[key.lower()]
	key = input()
	if key == "Пока":
		break
	print(get_answer(key, dialog))

    


