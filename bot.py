from telegram.ext import Updater, CommandHandler

import setting

def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")


def main():
    upd = Updater(setting.TELEGRAM_API_KEY)
    start_handler = CommandHandler('start', start)
    upd.dispatcher.add_handler(start_handler)
    upd.start_polling()
    upd.idle()


if __name__ == '__main__':
    main()
