import telebot
import time

bot_token='1584434812:AAFocYO8lD9W-6th7B2Pb1PhvByDtrtO9pQ'
bot = telebot.TeleBot(token=bot_token)

@bot.message_handler(commands=['start'])
def send_welcome (message):
    bot.reply_to(message,'welcome!')

bot.polling()