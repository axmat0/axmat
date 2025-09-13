import telebot
from telebot import types
import random
bot = telebot.TeleBot('7971066735:AAFBQyn-DwYsSYXerzuirFYwCtJj-zaUs3s')
OWNER_ID = 1161212796

random_photos = [
    {"file": "ilkanaz1.jpg"},
    {"file": "ilkanaz2.jpg"},
    {"file": "ilkanaz3.jpg"},
    {"file": "ilkanaz4.jpg"},
    {"file": "ilkanaz5.jpg"},
    {"file": "ilkanaz6.jpg"},
    {"file": "ilkanaz7.jpg"},
    {"file": "ilkanaz8.jpg"},
    {"file": "ilkanaz9.jpg"},
    {"file": "ilkanaz10.jpg"},
    {"file": "ilkanaz11.jpg"},
    {"file": "ilkanaz12.jpg"},
    {"file": "ilkanaz13.jpg"},
    {"file": "ilkanaz14.jpg"},
    {"file": "ilkanaz15.jpg"},
    {"file": "ilkanaz16.jpg"},
    {"file": "ilkanaz17.jpg"},
    {"file": "ilkanaz18.jpg"},
    {"file": "ilkanaz19.jpg"},
    {"file": "ilkanaz20.jpg"},
    {"file": "ilkanaz21.jpg"},
    {"file": "ilkanaz22.jpg"},
    {"file": "ilkanaz23.jpg"},
    {"file": "ilkanaz24.jpg"},
    {"file": "ilkanaz25.jpg"},
    {"file": "ilkanaz26.jpg"},
    {"file": "ilkanaz27.jpg"},
    {"file": "ilkanaz28.jpg"}
]


random_music = [
    "https://open.spotify.com/track/7ttJlpT7JWSPOhgAxTREMW?si=c6c4a7e2450d45e6",
    "https://open.spotify.com/track/7ehlridFShJlbffVYA2zhU?si=16f717c166d0434f",
    "https://open.spotify.com/track/3A4FRzgve9BjfKbvVXRIFO?si=64a9e42b94644458",
    "https://open.spotify.com/track/4T3ssJ7h388Hif7k1I3wUa?si=01d2549abbd34676",
    "https://open.spotify.com/track/4VV9H9WwyCO5lGWgbC7t3U?si=4ce9fb49350c408c",
    "https://open.spotify.com/track/0SfTFs26Jp1kOcUWprH1U8?si=169eb87874bb45ea",
    "https://open.spotify.com/track/0KKkJNfGyhkQ5aFogxQAPU?si=c9403b81d2744134",
    "https://open.spotify.com/track/5G2kzeSTbozqWnkAZnKn4e?si=83a0ee16c92047ec",
    "https://open.spotify.com/track/3EaJDYHA0KnX88JvDhL9oa?si=93dee0fa3992412a",
    "https://open.spotify.com/track/63HHF9ZpCIisujKFk2rixR?si=9c72e951d7014139"
]

@bot.callback_query_handler(func=lambda call: True)
def handle_callback_query(call):
    if call.data == "photos":
        choice = random.choice(random_photos)
        with open(choice['file'], "rb") as photo:
            bot.send_photo(call.message.chat.id, photo)
            bot.answer_callback_query(call.id)

def menu(chat_id):
    markup = types.InlineKeyboardMarkup()
    random.choice(random_music)
    btn6 = types.InlineKeyboardButton('Фоточки📸', callback_data='photos')
    btn7 = types.InlineKeyboardButton('Мюзика🎶', url = random.choice(random_music))
    btn8 = types.InlineKeyboardButton('Слова поддержки❤️', callback_data='words')
    markup.add(btn6, btn7, btn8)
    bot.send_message(chat_id, 'Выбирай😸 \n📷Кнопка фоточки отправляет рандомные фотки наши, твои либо мои, чтобы ты вспомнила те моменты которые мы пережили вместе.\n🎶 А кнопочка мюзика отправляет тебя в страницу где рандомные песни которые хранят наши теплые воспоминания.\n❤️ Кнопочка слова поддержки не требует разьяснения)', reply_markup=markup)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton ('Привет,хорошо')
    btn2 = types.KeyboardButton ('Привет,плохо(')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id,'Привет жаным, как дела? Я создал этого бота тебе как подарочек, что-то по типу хэндмэйда но так как я люблю это делать)', reply_markup=markup)

@bot.message_handler(func=lambda message: True)
def handle_answer(message):

    if message.text == 'Привет,хорошо':
        bot.send_message(message.chat.id, 'Замечательно! Что хочешь сегодня?')
        menu(message.chat.id)

    elif message.text == 'Привет,плохо(':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn3 = types.KeyboardButton('Мне одиноко')
        btn4 = types.KeyboardButton('Мне грустно')
        btn5 = types.KeyboardButton('Я скучаю')
        markup.add(btn3, btn4, btn5)
        bot.send_message(message.chat.id, 'А что случилось жаным сол?', reply_markup=markup)
    elif message.text == 'Мне одиноко':
        bot.send_message(message.chat.id, 'You are not alone, im always with you even if i didnt, с тобой всегда я на связи, я никогда о тебе не забываю, чтобы это доказать я создал этого бота) Но даже так с тобой всегда твоя семья которая очень сильно тебя любит, когда я увидел в первый раз твою маму, я видел как она переживает за тебя и относилась ко мне с осторожностью. Так что давай лучше поднимем настроение и выбери один из ниже перечисленных вариантов)')
        bot.send_message(message.chat.id, 'CAACAgIAAxkBAAEPXQ1oxUXxZddTgfN1MQ89HXgRDnGCDwACqj4AApK84Uu5NL7smgY91zYE')
        menu(message.chat.id)
    elif message.text == 'Мне грустно':
        bot.send_message(message.chat.id, 'Жаным сол, все будет хорошо, как только я закончу свое обучение мы начнем исполнять наши мечты, мы полетим в Корею, Японию и даже в Швейцарию, только мы вдвоем представь🤩 \nЕще раз напомню что я тебя люблю сильнее всего на свете и если букет тебе или маме то я выберу тебе), Если тебе ну уж очень грустно то напиши мне обязательно хорошо?')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPXQJoxUWhxb0IAAEateZ_WniJuxemcVoAAhIYAAJcOTlIZpd5giRj5oY2BA')
        menu(message.chat.id)
    elif message.text == 'Я скучаю':
        bot.send_message(message.chat.id, 'Я тоже очень сильно скучаю, всегда помни об этом. И это не повод грустить! Это повод провести это время с пользой и стать лучшей версией себя. Я верю в тебя и очень тобой горжусь, я знаю что ты делаешь все что в твоих силах и я горжусь этим, ты большой большой молодец💛')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEPW_VoxFe4aOrpJ3-UivUMBVr6grMMpQAC8wADVp29Cmob68TH-pb-NgQ')
        menu(message.chat.id)
bot.polling(non_stop = True)