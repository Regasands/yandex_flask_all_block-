import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
import json
import os
import random
from telegram import ReplyKeyboardMarkup

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'

from googletrans import Translator


async def start(update, context):
    context.user_data['translate'] = 'en'
    context.user_data['dest'] = 'ru'
    reply_keyboard = [['/swith_en_ru', '/swith_ru_en']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text('Отлично, введи текст чтобы перевести или смени язык!', reply_markup=markup)


async def translate(update, context):
    try:
        src = context.user_data['translate']
        dest = context.user_data['dest']
        translator = Translator()
        translation = await translator.translate(update.message.text, src=dest, dest=src)
        await update.message.reply_text(translation.text)  # Привет, мир!
    except Exception as e:
        await update.message.reply_text(f'{e}')


async def swith_en_ru(update, context):
    context.user_data['translate'] = 'ru'
    context.user_data['dest'] = 'en'


async def swith_ru_en(update, context):
    context.user_data['translate'] = 'en'
    context.user_data['dest'] = 'ru'


def main():
    app = Application.builder().token(TOKEN).build()
    text_handler = MessageHandler(filters.TEXT, translate)
    app.add_handler(CommandHandler('start',  start))
    app.add_handler(CommandHandler('swith_en_ru',  swith_en_ru))
    app.add_handler(CommandHandler('swith_ru_en',  swith_ru_en))
    app.add_handler(text_handler)
    app.run_polling()

if __name__ == '__main__':
    main()
