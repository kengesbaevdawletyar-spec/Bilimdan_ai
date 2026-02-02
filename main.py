import logging
from flask import Flask
from threading import Thread
import google.generativeai as genai
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# 1. Veb-server (Render-de bot oyaq turıwı ushın kerek)
app = Flask('')

@app.route('/')
def home():
    return "Bot islep tur!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. Sazlamalar (Kiltlerińizdi mınan jerge qoyıń)
TELEGRAM_TOKEN = "8479015329:AAGyW_Fueu1gLIf2pf73nM9xKyxppGYNNpo"
GEMINI_API_KEY = "BUL_JERGE_ÓZIŃIZDIŃ_GEMINI_KILTIŃIZDI_QOYIŃ"

# Gemini-di sazlaw
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Bot hám Dispatcher
bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalamu alaykum! Men Gemini biypul AI botpaman. \nLatin yamasa kirill álippesinde jazsańız boladı!")

@dp.message_handler()
async def chat_with_gemini(message: types.Message):
    try:
        # Botqa tildi hám álippeni saqlaw boyınsha kórsetpe
        instructions = (
            "Sen aqıllı járdemshisiń. Paydalanıwshı qaysı tilde hám q
