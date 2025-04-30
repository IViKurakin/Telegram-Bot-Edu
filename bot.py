import telebot
from telebot import types
import requests
import wikipedia

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_gigachat.chat_models import GigaChat

token='7805823166:AAFg57HTvzDI7rMstK7JpkR-aqyHJ-ggrEU'
newsAPI='a6a607d662ab41b29ef6a4da5713afba'
wikipedia.set_lang('ru')
# Создание бота
bot = telebot.TeleBot(token)
# Функция, обрабатывающая команду /start
@bot.message_handler(commands=['start'])
def start(mybot, res=False):
    mymarkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1=types.KeyboardButton('Погода')
    button2=types.KeyboardButton('Википедия')
    button3=types.KeyboardButton('Giga Болтун')
    mymarkup.add(button1)
    mymarkup.add(button2)
    mymarkup.add(button3)
    bot.send_message(mybot.chat.id, 'Я на связи. Напиши мне что-нибудь.', reply_markup=mymarkup)

# Функция трансляции прогноза погоды
def Weather(message):
    keyAPI='c421857110df2b1e6445d5eafd267825'
    query=f"http://api.openweathermap.org/data/2.5/weather?q={message.text}&APPID={keyAPI}&units=metric";
    weather=requests.get(query).json()
        # Иконка
    icon=weather['weather'][0]['icon']
        # Температура
    temperature=round(weather['main']['temp'])
    if temperature>0:
        temperature=f'+{temperature}'
        # Скорость ветра
    wind_speed=round(weather['wind']['speed'])
        # Направление ветра
    wind_deg=weather['wind']['deg']
    if wind_deg>=337 or wind_deg<22:
        deg='северный'
    if wind_deg>=22 and wind_deg<67:
        deg='северо-восточный'
    if wind_deg>=67 and wind_deg<112:
        deg='восточный'
    if wind_deg>112 and wind_deg<157:
        wind_deg='юго-восточный'
    if wind_deg>=157 and wind_deg<202:
        deg='южный'
    if wind_deg>=202 and wind_deg<247:
        deg='юго-западный'
    if wind_deg>=247 and wind_deg<=292:
        deg='западный'
    if wind_deg>292 and wind_deg<337:
        deg='cеверо-западный'
    
    bot.send_message(message.chat.id, f'Сейчас в г. {message.text} {temperature}°C, ветер {deg}, {wind_speed} м/c.' )
    bot.send_photo(message.chat.id, open(f'img/{icon}.png', 'rb'))

# Функция включения Википедии
def Wiki(message):
    try:
        article=wikipedia.page(message.text)
        wikitext=article.content[:3000]
        wikimask=wikitext.split('.')
        wikimask=wikimask[:-1]
        wiki=''
        for x in wikimask:
            if not('==' in x):
                if(len((x.strip()))>3):
                    wiki=wiki+x+'.'
            else:
                break
        bot.send_message(message.chat.id, wiki)
    except Exception as e:
        return 'В Википедии нет статьи по вашему запросу'

# Болталка
@bot.message_handler(func=lambda message: True)
def Speak(message):
    if message.text in ["Стоп!", "Хватит!", "Stop!"]:
        bot.send_message(message.chat.id, "Диалог завершён")
        return
    giga = GigaChat(
    # Для авторизации запросов используйте ключ, полученный в проекте GigaChat API
    credentials="MTRiMjdmNGYtZWEyNS00ODZkLWE3MGYtNjQ3YWU3YTI3MDY4OjlmMWZjNGMzLWMwOGUtNDJhOC05NTVlLTIwNDI3NjZhZTRjMw==",
    verify_ssl_certs=False,
    )
    messages = [
    SystemMessage(
        content="Ты эмпатичный бот-психолог, который помогает пользователю решить его проблемы.")
    ]
    messages.append(HumanMessage(content=message.text))
    res = giga.invoke(messages)
    messages.append(res)
    bot.send_message(message.chat.id, res.content )
    


# Получение сообщений от пользователя
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text=='Погода':
            bot.send_message(message.chat.id, 'В каком городе показать погоду? ')
            bot.register_next_step_handler(message, Weather)
    elif message.text=='Википедия':
            bot.send_message(message.chat.id, 'Введите свой запрос для Википедии: ')
            bot.register_next_step_handler(message, Wiki)
    elif message.text=='Giga Болтун':
            bot.send_message(message.chat.id, 'Введите свой запрос для Болтуна: ')
            bot.register_next_step_handler(message, Speak)
    else:
        bot.send_message(message.chat.id, f'Вы написали {message.text}')

# Запуск бота
bot.polling(non_stop=True, interval=0)
