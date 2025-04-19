import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
import json
import os

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)
logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'

async def send_file(update, context):
    await update.message.reply_text('Отправьте JSON-файл.')
    return 1

async def get_file(update, context):
    file = update.message.document
    if not (file.mime_type == 'application/json' or file.file_name.endswith('.json')):
        await update.message.reply_text("Пожалуйста, отправьте JSON-файл!")
        return ConversationHandler.END

    file_path = f"temp_{file.file_name}"
    try:
        
        downloaded_file = await context.bot.get_file(file.file_id)
        await downloaded_file.download_to_drive(file_path)

        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
                
        if "test" not in data:
            await update.message.reply_text("Ошибка: в JSON нет ключа 'test'!")
            return ConversationHandler.END

        await update.message.reply_text(f"Файл обработан! Первый вопрос: {data['test'][0]['question']}, нажми /start для начала")
        context.user_data['json_data'] = data['test']  # Сохраняем данные

    except json.JSONDecodeError as e:
        await update.message.reply_text(f"Ошибка в JSON: {e}\nПроверьте, что файл валидный.")
    except Exception as e:
        await update.message.reply_text(f"Ошибка: {e}")
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

    return ConversationHandler.END

async def start(update, context):
    context.user_data['number'] = 0
    context.user_data['properly'] = 0
    question = context.user_data['json_data']
    
    await update.message.reply_text(f"Отлино ответь на первый вопрос")
    await update.message.reply_text(f'{question[0]['question']}')
    return 1

async def asnwer(update, context):
    try:
        number = context.user_data['number']
        question = context.user_data['json_data'][number]
        answer = update.message.text
        if answer == question['response']:
            await update.message.reply_text('Отлично, верно ')
            context.user_data['properly'] += 1
        else:
            await update.message.reply_text(f'Не верно, ответ {question["response"]} ')
        if number + 1 >= len(context.user_data['json_data']):
            await update.message.reply_text(f'Отлично, тест завершен коли-во правильных ответов {context.user_data['properly'] }')
            return ConversationHandler.END
        else:
            context.user_data['number'] += 1

            await update.message.reply_text(f'Следующий вопрос, {context.user_data['json_data'][number + 1]['question']}')

        return 1
    except Exception as e:
        await update.message.reply_text(f'Что-то не так пошло {e}')
        return 1




def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('send_file', send_file)],
        states={1: [MessageHandler(filters.Document.ALL, get_file)]},
        fallbacks=[]
    )
    conv_handlers = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={1: [MessageHandler(filters.TEXT & ~filters.COMMAND, asnwer)],},
        fallbacks=[]
    )
    app.add_handler(conv_handler)
    app.add_handler(conv_handlers)
    app.run_polling()

if __name__ == '__main__':
    main()
