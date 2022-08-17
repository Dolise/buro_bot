import logging
import os
import json
import telebot
from telebot import types
import buttons
from flask import Flask, request

allowed_users = json.loads(os.getenv("ALLOWED_IDS"))
token = os.getenv("TOKEN")
server = Flask(__name__)


bot = telebot.TeleBot(token)


def permission(message):
    if message.chat.id in allowed_users:
        return True
    return False


@bot.message_handler(commands=["start"])
def start(message):
    if not permission(message):
        return
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    markup.add(*buttons.default_buttons)
    bot.send_message(
        message.chat.id,
        "Поздравляем! Вы подписались на BALANCE BURO bot."
        "\n\n"
        "Используйте /off чтобы приостановить подписку.",
        reply_markup=markup
    )


@bot.message_handler(content_types="text")
def answer(message):
    if not permission(message):
        return
    if message.text == buttons.refer_cases_guide.text:
        bot.send_message(
            message.chat.id,
            "Тут у нас инструкация по передаче дел для дизайнеров и проджект-менеджеров"
            "\n\n"
            "https://clck.ru/sc4Ax"
        )
    elif message.text == buttons.yandex_disc.text:
        bot.send_message(
            message.chat.id,
            "Лови ссылочку на Яндекс Диск!"
            "\n\n"
            "https://disk.yandex.ru/d/0VNn3egXzagtuA"
        )
    elif message.text == buttons.motion_technical_task.text:
        bot.send_message(
            message.chat.id,
            "Анимируемся! Пишем ТЗ по шаблону в этом доке — https://clck.ru/sXMqM"
            "\n\n"
            "Заполняя форму не забудь, что ТЗ должно соответствовать регламенту:"
            "\n\n"
            "1) Новые ТЗ ставятся наверх документа."
            "\n\n"
            "2) Над рамкой с ТЗ обязательно пишем «Актуальная задача» и четкий дедлайн финала (дата и время)."
            "\n\n"
            "3) Пишем вводные данные: длительность анимации, формат."
            "\n\n"
            "4) Прикрепляем ссылку на PSD файл, загруженный на диск."
            "\n\n"
            "5) Прописываем техническое задание. Что нам нужно, кружочек для телеграмм, анимация для сайта или что-то другое? "
            "\n\n"
            "6) Составляем четкий сценарий анимации по кадрам и прикрепляем референсы/шрифты, если есть."
            "\n\n"
            "7) Как только задача закрывается — пишем «выполнено» над рамкой с ТЗ."
        )
    elif message.text == buttons.miro_table.text:
        bot.send_message(
            message.chat.id,
            "Есть идеи по апдейту офиса? Кайф!"
            "\n\n"
            "Скорее заполняй свою доску в miro https://clck.ru/sbzDs"
            "\n"
            "Пс, следи за регламентами 👀"
        )
    elif message.text == buttons.work_report.text:
        bot.send_message(
            message.chat.id,
            "Ура, пятница!"
            "\n\n"
            "Заполни отчёт и не забудь отправить мем недели!"
            "\n\n"
            "https://forms.gle/UL6hVR1nALW9TLgS6"
        )


@server.route('/' + token, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://balanceburo.herokuapp.com' + token)
    return "!", 200


if __name__ == "__main__":
    print("STARTED")
    logging.basicConfig(level=logging.INFO)
    server.run(host="0.0.0.0", port=5000)
