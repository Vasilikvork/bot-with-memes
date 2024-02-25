from bs4 import BeautifulSoup
from keys import token
from ref_get import *
from telebot import types
import telebot  
import requests
import random


bot=telebot.TeleBot(token)
    
@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("❓Помощь")
    btn2 = types.KeyboardButton("💾Возможности")
    markup.row(btn1, btn2)
    bot.send_message(message.chat.id, 'Приветствую тебя о юный искатель древнего знания чем я могу помочь? Чтобы узнать больше нажми на кнопочку "❓Помощь"', reply_markup=markup)
        
@bot.message_handler(content_types=['text'])
def help_message(message):
    if message.chat.type == 'private':
        if message.text == "❓Помощь":
            bot.send_message(message.chat.id, (("Если считаете что что-то идет не так отправте боту комманду: /start - перезагрузка бота. Если же хотите воспользоваться функциями нашего бота то жмите на кнопку - 💾Возможности")))
        elif message.text == "😂Мемы":
            url = meme_get()
            bot.send_photo(message.chat.id, url)
        elif message.text == "💾Возможности":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("🥸Анекдоты")
            btn2 = types.KeyboardButton("😂Мемы")
            btn3 = types.KeyboardButton("🍞Карикатуры")
            btn4 = types.KeyboardButton("👮‍♂️Фразы")
            back = types.KeyboardButton("⬅️Назад")
            markup.row(btn1, btn2, btn3, btn4, back)
            bot.send_message(message.chat.id, 'Вы всегда можете вернуться с помощью кнопки "⬅️Назад"', reply_markup=markup)
        elif message.text == "⬅️Назад":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("❓Помощь")
            btn2 = types.KeyboardButton("💾Возможности")
            markup.row(btn1, btn2)
            bot.send_message(message.chat.id, 'Вы вернулись назад', reply_markup=markup)
        elif message.text == "🥸Анекдоты":
            bot.send_message(message.chat.id, anekdot_get())
        elif message.text == "🍞Карикатуры":
            url = karikature_get()
            bot.send_photo(message.chat.id, url)
        elif message.text == "👮‍♂️Фразы":
            bot.send_message(message.chat.id, phrase_get())
        else:
            bot.send_message(message.chat.id, "Пользуйтесь кнопками или скопируйте текст с кнопок🙂")
bot.polling(non_stop=True, timeout=None)
