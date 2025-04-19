import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from datetime import datetime
import random
from telegram import ReplyKeyboardMarkup, Update, ReplyKeyboardRemove

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'

TIMER = 5  # таймер на 5 секунд



def remove_job_if_exists(name, context):
    """Удаляем задачу по имени.
    Возвращаем True если задача была успешно удалена."""
    current_jobs = context.job_queue.get_jobs_by_name(name)
    if not current_jobs:
        return False
    for job in current_jobs:
        job.schedule_removal()
    return True


async def start(update, context):
    reply_keyboard = [['/dice', '/timer']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
    await update.message.reply_text('отлично ввыбери действие ', reply_markup=markup)


async def dice(update, context):
    reply_keyboard = [['Кинуть один шестигранный кубик'],
                      ['кинуть 2 шестигранных кубика одновременно'],
                      ['кинуть 20-гранный кубик'],
                      ['вернуться назад.'],
                      ]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
    "Подготавливаем кубики",
    reply_markup=ReplyKeyboardRemove())

    await update.message.reply_text('отлично выбери действие ', reply_markup=markup)


async def timer(update, context):
    reply_keyboard = [['30 секунд'], ['1 минута'], ['5 минут '], ['вернуться назад.']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    await update.message.reply_text(
    "Подготавливаем таймеры",
    reply_markup=ReplyKeyboardRemove())
    await update.message.reply_text('отлично выбери действие ', reply_markup=markup)


async def responce_test(update, context):
    text = update.message.text
    if text == 'Кинуть один шестигранный кубик':
        await update.message.reply_text(f'{random.randint(1, 6)}') 
        return
    elif text == 'кинуть 2 шестигранных кубика одновременно':
        await update.message.reply_text(f'{random.randint(1, 6)}, {random.randint(1, 6)}')
        return
    elif text == 'кинуть 20-гранный кубик':
        await update.message.reply_text(f'{random.randint(1, 20)}')
        return
    elif text == 'вернуться назад.':

        reply_keyboard = [['/dice', '/timer']]
        markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)
        await update.message.reply_text(
        "Подготавливаем дейсвтия",
        reply_markup=ReplyKeyboardRemove())

        await update.message.reply_text('отлично ввыбери действие ', reply_markup=markup)
        return
    elif text == '30 секунд':
        context.user_data['time'] = 30
    elif text == '1 минута':
        context.user_data['time'] = 60
    elif text == '5 минут':
        context.user_data['time'] = 300

    await set_timer(update, context)




# Обычный обработчик, как и те, которыми мы пользовались раньше.
async def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.effective_message.chat_id
    timer_time = float(context.user_data['time'])



    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(task, timer_time, chat_id=chat_id, name=str(chat_id), data=timer_time)

    text = f'засек {timer_time}'
    await update.message.reply_text(
        "Подготавливаем отмену таймеру",
    reply_markup=ReplyKeyboardRemove())


    markup = ReplyKeyboardMarkup([['/close']], one_time_keyboard=True)
    await update.message.reply_text(text, reply_markup=markup)




async def task(context):
    job = context.job
    await context.bot.send_message(context.job.chat_id, text=f'{job.data} истекло.')


async def close(update, context):
    """Удаляет задачу, если пользователь передумал"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер отменен!' if job_removed else 'У вас нет активных таймеров'
    await update.message.reply_text(text)



def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("timer", timer))
    app.add_handler(CommandHandler("close", close))
    app.add_handler(CommandHandler('dice', dice))
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, responce_test))

    app.run_polling()


if __name__ == '__main__':
    main()

