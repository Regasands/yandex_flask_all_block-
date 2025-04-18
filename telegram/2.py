import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from datetime import datetime


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'


async def date(update, context):
    now = datetime.now()
    await update.message.reply_text(now.strftime("%d.%m.%Y"))


async def time(update, context):
    now = datetime.now()
    await update.message.reply_text(now.strftime("%H:%M:%S"))




def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("date", date))
    app.add_handler(CommandHandler("time", time))
    app.run_polling()


if __name__ == '__main__':
    main()
