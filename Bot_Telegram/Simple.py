#!/usr/bin/env python
# -*- coding: utf-8 -*-

from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime
now = datetime.now().ctime()

# importing modules
import requests
from bs4 import BeautifulSoup

# get URL html
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

def start(update, context):
    # Send a message when the command /start is issued.
    update.message.reply_text('Hola Javi, qué tal!?')

def help(update, context):
    # Send a message when the command /help is issued.
    update.message.reply_text(
        'Le has dado a Help! En breve este help te ayudará de verdad, por ahora te mando una foto de Nina Williams!')
    url = "https://external-content.duckduckgo.com/iu/?u=http://flashfoxy.com/wp-content/uploads/2019/05/IMG_4930-768x1024.jpg&f=1&nofb=1"
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def news(update, context):
    now = datetime.now().ctime()
    update.message.reply_text('Mensaje el: ' + str(now))

def main():
    updater = Updater('1374998996:AAHrFtkZ30MlmKUIvFCpwWYp0BGJLQkEBHk')

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('help', help))
    updater.dispatcher.add_handler(CommandHandler('news', news))

    updater.start_polling()
    updater.idle()

if '__main__' == '__main__':
    main()

