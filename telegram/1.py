import logging
from telegram.ext import Application, MessageHandler, filters

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'


async def echo(update, context):
    await update.message.reply_text(f'Я получил сообщение {update.message.text}')



def main():
    app = Application.builder().token(TOKEN).build()

    text_handler = MessageHandler(filters.TEXT, echo)
    app.add_handler(text_handler)
    app.run_polling()


if __name__ == '__main__':
    main()
