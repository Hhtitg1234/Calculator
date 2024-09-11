import telebot
import numexpr as ne
from telebot import types

TOKEN = '7399431243:AAFzCCvoGGTgnmq0EKV2_Qc_IxWKtLTbYl4'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def greetings(message):
    markup = types.InlineKeyboardMarkup()
    strt_btn_1 = types.InlineKeyboardButton('Calculate 1 primer', callback_data='1 primer')
    markup.add(strt_btn_1)
    bot.send_message(message.chat.id, f'Здравствуйте, {message.from_user.first_name}! Что бы вы хотели выбрать?',
                     reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback_message(call):
    if call.data == '1 primer':
        quest_stage_1(call.message)
    elif call.data == 'cancel':
        quest_stage_2(call.message)


def quest_stage_1(message):
    bot.reply_to(message, 'Напишите пример, который нужно решить: ')


@bot.message_handler(func=lambda message: True)
def private_message_forward(message):
    markup = types.InlineKeyboardMarkup()
    btn_1 = types.InlineKeyboardButton('End calculate', callback_data='cancel')
    markup.row(btn_1)
    primer = message.text
    result = ne.evaluate(primer)
    print(result)
    print(type(result))
    bot.send_message(message.chat.id, f'The result is: {result}', reply_markup=markup)
# greetings(message)


def quest_stage_2(message):
    greetings(message)


bot.infinity_polling()
