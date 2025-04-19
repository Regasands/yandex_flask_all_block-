import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler
from datetime import datetime


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


# Обычный обработчик, как и те, которыми мы пользовались раньше.
async def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.effective_message.chat_id
    try:
        timer_time = float(context.args[0])
    except Exception:
        timer_time = TIMER



    job_removed = remove_job_if_exists(str(chat_id), context)
    context.job_queue.run_once(task, timer_time, chat_id=chat_id, name=str(chat_id), data=timer_time)

    text = f'Вернусь через {timer_time} с.!'
    if job_removed:
        text += ' Старая задача удалена.'
    await update.effective_message.reply_text(text)



async def task(context):
    job = context.job
    """Выводит сообщение"""
    await context.bot.send_message(context.job.chat_id, text=f'КУКУ! {job.data}. прошли!')


async def unset(update, context):
    """Удаляет задачу, если пользователь передумал"""
    chat_id = update.message.chat_id
    job_removed = remove_job_if_exists(str(chat_id), context)
    text = 'Таймер отменен!' if job_removed else 'У вас нет активных таймеров'
    await update.message.reply_text(text)



def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("set", set_timer))
    app.add_handler(CommandHandler("unset", unset))
    app.run_polling()


if __name__ == '__main__':
    main()
