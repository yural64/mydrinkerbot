import telebot # библиотека для создания тг бота
import datetime # работа с датой и временем, в т.ч. форматирование при выводе
import time # позволяет приостанавливать программу на заданное время
import threading # модуль для работы с потоками
import random


bot = telebot.TeleBot('7400243966:AAEieleLsjTOnT_XqRn7eW8pciVk3XTYHiU') # прописываем свой токен для бота


# Декораторы используем для создания команд

@bot.message_handler(commands=['start']) # декоратор для команды start
def start_message(message): # message - переменная, в кот. сохр. инф. о пользователе, кот. вызвал команду
    bot.reply_to(message, 'Привет! Я чат бот, который будет напоминать тебе пить водичку!')
    reminder_thread = threading.Thread(target=send_reminders, args=(message.chat.id,)) # поток reminder_thread для запуска напоминания
    reminder_thread.daemon = True  # Устанавливаем поток как демона, чтобы он завершался вместе с основным потоком
    reminder_thread.start() # запуск потока

# Функция, которая выводит рандомный факт о воде

@bot.message_handler(commands=['fact']) # декоратор для команды fact
def fact_message(message):
    facts = ["**Аномальные свойства воды**: Одним из самых известных является то, что вода в твердом состоянии (лед) менее плотная, чем в жидком состоянии.",
            "**Вода — универсальный растворитель**: Вода обладает высокой способностью растворять многие вещества.",
            "**Тройная точка воды**: Тройная точка воды — это уникальное состояние, при котором вода может существовать одновременно в трех фазах: твердой, жидкой и газообразной. Это происходит при температуре 0.01°C (273.16 K) и давлении 611.657 паскалей (около 0.006 атмосферы)."]
    random_fact = random.choice(facts)
    bot.reply_to(message, f'Интересный факт о воде: {random_fact}')

# Функция напоминания

def send_reminders(chat_id):
    rem_1 = "07:00"
    rem_2 = "09:00"
    rem_3 = "12:00"
    rem_4 = "15:00"
    rem_5 = "18:00"
    rem_6 = "21:00"
    rem_7 = "23:00"
    reminder_times = [rem_1, rem_2, rem_3, rem_4, rem_5, rem_6, rem_7]
    while True: # бесконечный цикл
        now = datetime.datetime.now().strftime('%H:%M')
        if now in reminder_times:
            bot.send_message(chat_id, "Пора выпить стакан воды!")
            time.sleep(61)
        time.sleep(1)


bot.polling(none_stop=True) # запускаем бот (в самом низу программы)