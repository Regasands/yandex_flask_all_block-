'''    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    map_api_server = "https://static-maps.yandex.ru/v1?"
    
    params = {'ll': f'{koord[1]},{koord[0]}', 'spn': f'0.1,0.1',  'apikey': apikey, 'lang': 'ru_Ru'}
    response = requests.get(map_api_server, params=params)
    print(response.url)
    image = BytesIO(response.content)
    '''

import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from datetime import datetime
import requests
from io import BytesIO

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)

TOKEN = '7872226772:AAE_yUSmr-VgTNYdncaVBDpf2m3BuaWAn8I'



async def start(update, context):
    await update.message.reply_text('Привет, это бот отправляет картинки по  адрессу, жду от тебя адресс')


async def get_image(update, context):
    # первая часть будем получать корды йоу
    text = update.message.text  
    
    server_address = 'http://geocode-maps.yandex.ru/1.x/?'
    api_key = '8013b162-6b42-4997-9691-77b7074026e0'
    geocoder_request = f'{server_address}apikey={api_key}&geocode={text}&format=json'

    response = requests.get(geocoder_request)
    
    if response:
        json_response = response.json()
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        # Координаты центра топонима:
        koord = toponym["Point"]["pos"].split()
    else:
        await update.message.reply_text("Ошибка выполнения запроса:")

        await update.message.reply_text(f"{geocoder_request}")

        await update.message.reply_text(f"Http статус: {response.status_code} ({response.reason})")
        return
    if text.lower() not in toponym_address.lower():
        await update.message.reply_text('Ничего не найдено')
        return 

    # вторая часть брошный яндекс

    apikey = "f3a0fe3a-b07e-4840-a1da-06f18b2ddf13"
    map_api_server = "https://static-maps.yandex.ru/v1?"
    params = {
        'll': f'{koord[0]},{koord[1]}',  # Центр карты
        'spn': '1,1',                     # Масштаб
        'pt': f'{koord[0]},{koord[1]},vkbkm',  # Метка (vkbkm — тип метки)
        'apikey': apikey,
        'lang': 'ru_RU'}
    
    response = requests.get(map_api_server, params=params)
    image = BytesIO(response.content)
    await update.message.reply_photo(photo=image, caption=f"📍 Координаты: {koord[0]}, {koord[1]}\nМасштаб: 1x1 градус.Место {toponym_address}")



def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.TEXT, get_image))
    app.run_polling()


if __name__ == '__main__':
    main()


