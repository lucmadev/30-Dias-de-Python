import telebot
from dotenv import load_dotenv
import os

load_dotenv()

# Reemplazá con tu token de BotFather
TOKEN = os.getenv("TOKEN")

bot = telebot.TeleBot(TOKEN)

# Respuesta al comando /start
@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "👋 ¡Hola! Soy tu primer bot en Python")

# Respuesta a cualquier mensaje de texto
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, f"Me dijiste: {message.text}")

print("🤖 Bot funcionando... Abrí Telegram y hablale.")
bot.infinity_polling()