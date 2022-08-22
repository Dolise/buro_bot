from telebot import types

refer_cases_guide = types.KeyboardButton("Гайд передачи дел")
yandex_disc = types.KeyboardButton("Яндекс Диск")
motion_technical_task = types.KeyboardButton("Составить ТЗ для motion-дизайна")
miro_table = types.KeyboardButton("Доска miro по апдейту офиса")
work_report = types.KeyboardButton("Рабочий отчет")
sticker = types.KeyboardButton("Поднять настроение")
presentations = types.KeyboardButton("Шаблон для верстки презентаций")

default_buttons = [refer_cases_guide, yandex_disc, presentations, motion_technical_task, miro_table, work_report, sticker]


easy_presentation = types.KeyboardButton("Простая")
default_presentation = types.KeyboardButton("Стандартная")
presentation_buttons = [easy_presentation, default_presentation]


main_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
main_markup.add(*default_buttons)

presentation_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
presentation_markup.add(*presentation_buttons)