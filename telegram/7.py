import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from datetime import datetime


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'

poem1 = [
    "У лукоморья дуб зелёный,",
    "Златая цепь на дубе том:",
    "И днём и ночью кот учёный",
    "Всё ходит по цепи кругом."
]

async def start(update, context):
    await update.message.reply_text(poem1[0])
    context.user_data['number'] = 1
    return 1


async def first_response(update, context):
    text = update.message.text
    number = context.user_data['number']
    if number >= 3:
        if text == poem1[number]:
            await update.message.reply_text('Я поздравляю тебя , ты очень крутой /start начнем заново ')
            return ConversationHandler.END

    if text == poem1[number]: 
        await update.message.reply_text(poem1[number + 1])
        context.user_data['number'] = 3
    else:
        await update.message.reply_text('Нет, это не так , посмори верную строку /suphler')
    return 1 

async def suphler(update, context):
    number = context.user_data['number']
    await update.message.reply_text(poem1[number])
    return 1



async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



def main():
    app = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
    entry_points=[CommandHandler('start', start)],
    states={
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response),
            CommandHandler(('suphler'), suphler)],
    },
    fallbacks=[CommandHandler('stop', stop)]
    )

    app.add_handler(conv_handler)

    app.run_polling()


if __name__ == '__main__':
    main()


