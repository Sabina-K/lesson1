dialog = {"привет":"привет","как дела?":"хорошо, а у тебя?"}
def chatty(key, dia):
	return dia[key]
key = input()
print(chatty("как дела?",dialog))