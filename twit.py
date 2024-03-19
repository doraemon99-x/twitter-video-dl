import argparse

import src.twitter_video_dl.twitter_video_dl as tvdl
import telebot

TOKEN = '6529702195:AAFuDZiOiOXh116Ohsg3wxI86_ymDmUZQYc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Halo! Saya adalah bot Anda. Kirimkan saya URL Twitter dan saya akan mendownload videonya untuk Anda.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    twitter_url = message.text
    file_name = "twittervid.mp4"

    tvdl.download_video(twitter_url, file_name)
    video = open(file_name, 'rb')
    bot.send_video(message.chat.id, video)

bot.polling()
