from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import logging
from datetime import datetime
import time
import random
import settings

logging.basicConfig(filename = "logs.log", level = logging.DEBUG)

vk_session = VkApi(token = settings.token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, settings.group_id, wait = 60)

keyboard_command = {
    "beginning": "Начать",
    "document": "Заказать документ",
    "consulting": "Заказать консультацию"
}

message_to_user = {
    "beginning": "Привет, выберите опцию",
    "document": "Опишите подробно, какой документ вам нужен",
    "consulting": "Опишите подробно, какая консультация вам требуется",
    "unknown_command": "Извините, не знаю такой команды. Попробуйте ещё раз"
}

def create_keyboard(response):
    keyboard = VkKeyboard(one_time = False) #параметр False не закрывает клавиатуру после ответа на сообщение, True - закрывает

    if response == keyboard_command["beginning"]: #response - переменная функции, 
        keyboard.add_button(keyboard_command["document"], color = VkKeyboardColor.NEGATIVE) #primary - синяя, secondary - белая, negative - красная, positive - зелёная
        keyboard.add_button(keyboard_command["consulting"], color = VkKeyboardColor.POSITIVE)
    elif response == keyboard_command["document"]:
        keyboard.add_button('Кнопка 3', color = VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Кнопка 4', color = VkKeyboardColor.POSITIVE)
    elif response == keyboard_command["consulting"]:
        keyboard.add_button('Кнопка 5', color = VkKeyboardColor.NEGATIVE)
        keyboard.add_button('Кнопка 6', color = VkKeyboardColor.POSITIVE)
    else:
        keyboard.add_button(keyboard_command["beginning"], color = VkKeyboardColor.NEGATIVE)
    
    keyboard = keyboard.get_keyboard()
    # print(keyboard)
    return keyboard

def send_messages(id_type, id, message_to_user, keyboard = None, attachment = None):
    vk_session.method('messages.send', {id_type: id, 'message': message_to_user, 'random_id': random.randint(-2147483648, +2147483648), 'keyboard': keyboard})

def log_incoming_msg(message, user):
    return f'Входящее сообщение. Дата: {str(datetime.strftime(datetime.now(), "%d.%m %H:%M:%S"))}, \n сообщение: {message}, \n ID пользователя: {user} \n'

def log_outcoming_msg(message, user):
    return f'Исходящее сообщение. Дата: {str(datetime.strftime(datetime.now(), "%d.%m %H:%M:%S"))}, \n сообщение: {message}, \n ID пользователя: {user} \n'

def answer_to_user(message_from_user):
    if message_from_user in keyboard_command.values():
        for keys in keyboard_command.keys():
            if message_from_user == keyboard_command[keys]:
                sending_message = message_to_user[keys]
                logging.info(log_outcoming_msg(sending_message, event.obj.from_id))
                return send_messages('user_id', event.obj.from_id, sending_message, show_keyboard)
    else:
        sending_message = message_to_user["unknown_command"]
        logging.info(log_outcoming_msg(sending_message, event.obj.from_id))
        return send_messages('user_id', event.obj.from_id, sending_message, show_keyboard)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            logging.info(log_incoming_msg(event.obj.text, event.obj.from_id))
            message_from_user = event.obj.text
            show_keyboard = create_keyboard(message_from_user)
            if event.from_user:
                time.sleep(2)
                answer_to_user(message_from_user)