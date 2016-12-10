def ask_user(answers):
    user_input = input()
    answer = get_answer(user_input,answers)
    if not answers.get(user_input):
        bot.sendMessage(update.message.chat_id, text="Не понимаю((. Я только учусь")
    else:
        bot.sendMessage(update.message.chat_id, answer)
