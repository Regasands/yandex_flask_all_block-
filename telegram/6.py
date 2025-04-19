import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from datetime import datetime


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'
DCITERS = {
    '1': ['2', 'skip'],
    '2': ['3'],
    '3': ['1', '4'],
    '4': ['1']
}
rooms = {
    '1': "Вход в музей. Здесь находится гардероб и информационная стойка",
    '2': "Зал древнего искусства: античные скульптуры, египетские артефакты",
    '3': "Зал средневековья: рыцарские доспехи, готические реликвии",
    '4': "Зал современного искусства: инсталляции, цифровые экспонаты",
}

async def start(update, context):
    context.user_data['last_room'] = '1'
    await update.message.reply_text('Приветствие: Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб! Опции перехода: Зал 1, Зал 2 или Выход (Введите 1, 2, 3, 4, skip)')
    return 1


async def first_response(update, context):
    text = update.message.text
    print(text)
    last_room = context.user_data.get('last_room', None)
    if text in DCITERS[last_room]:
        if text == 'skip':
            await update.message.reply_text("Ты покинул комнату")
            return ConversationHandler.END
        await update.message.reply_text('Поздравляю ты перешел в другую комнату !!')
        await update.message.reply_text(rooms[text])
        context.user_data['last_room'] = text
        return 1 
    await update.message.reply_text(f'Не верная комнаты {DCITERS} введи верную комнату твоя комната {last_room}')
    return 1 




async def stop(update, context):
    await update.message.reply_text("Всего доброго!")
    return ConversationHandler.END



def main():
    app = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
    # Точка входа в диалог.
    # В данном случае — команда /start. Она задаёт первый вопрос.
    entry_points=[CommandHandler('start', start)],

    # Состояние внутри диалога.
    # Вариант с двумя обработчиками, фильтрующими текстовые сообщения.
    states={
        # Функция читает ответ на первый вопрос и задаёт второй.
        1: [MessageHandler(filters.TEXT & ~filters.COMMAND, first_response)],
        # Функция читает ответ на второй вопрос и завершает диалог.
    },

    # Точка прерывания диалога. В данном случае — команда /stop.
    fallbacks=[CommandHandler('stop', stop)]
)

    app.add_handler(conv_handler)

    app.run_polling()


if __name__ == '__main__':
    main()

