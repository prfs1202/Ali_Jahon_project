import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto

bot = telebot.TeleBot('7011165972:AAHKtDYqY5NkeSCi7Bc_uAiS4NUNtKq9HB8')
import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')
django.setup()
from apps.models import User


@bot.message_handler(commands=['start'])
def start(message):
    user = User.objects.first()
    bot.send_message(message.chat.id, f'{bot.bot_id}')


bot.infinity_polling()
