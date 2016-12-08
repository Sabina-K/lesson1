from telegram.ext import Updater, CommandHandler, MessageHandler, Filters 
def greet_user(bot, update):
	print('Вызван/ start')
	bot.sendMessage(update.message.chat_id, text='Давай общаться!')
def show_error(bot, update, error):
    print('Update "{}" caused error "{}"'.format(update, error))


dialog = {"привет": "и тебе привет!", "как дела": "лучше всех", "пока":"увидимся"}
def talk_to_me(bot, update):
    print("Пришло сообщение: " + update.message.text)
    bot.sendMessage(update.message.chat_id, chat[key.lower])

   
def main():
	updater = Updater("302143395:AAECx2k80ruHuLhTYnYxj7w6lhpXUWqdYjQ")
	dp = updater.dispatcher
	dp.add_handler(CommandHandler("start", greet_user))
	dp.add_handler(MessageHandler([Filters.text], talk_to_me))
	dp.add_error_handler(show_error)
	updater.start_polling()
	updater.idle()
if __name__== '__main__':
    main()



