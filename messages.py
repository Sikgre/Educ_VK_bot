import json
import logging_rules
from handlers import answer, error, keyboard_command, incorrect_command
from keyboard import keyboard_choice
from vk_functions import VKMethods
import db_functions

'''
Функция write_message планируется для осуществления записей текстов диалогов.
Запись пока не реализована до конца
'''


def write_message(obj):
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(obj))


'''
Функция def_answer - обработчик команд с клавиатуры.
Принимает команды, вводимые с клавиатуры (или аналогичные текстовые)
и возвращает текст ответа на команду и клавиатуру, которая его сопровождает
Передаёт результат в функцию, связывающуюся с сервером по API,
которая задана в файле get_vk.py
'''


def check_keyboard_command(message_from_user):
    return bool(message_from_user in keyboard_command.values())


def check_cancel_order(message_from_user):
    return bool(message_from_user == keyboard_command["cancel"])


def check_create_order(message_from_user):
    return bool(message_from_user == keyboard_command["document"]
                or
                message_from_user == keyboard_command["consulting"])


def start_new_order(message_from_user, user):
    if message_from_user == keyboard_command["document"]:
        db_functions.add_order_document(user)
    elif message_from_user == keyboard_command["consulting"]:
        db_functions.add_order_consulting(user)


def cancel_order(message_from_user, user):
    if message_from_user == keyboard_command["cancel"]:
        db_functions.cancel_order(user)


def command_before_order(message_from_user, user):
    if check_create_order(message_from_user) is True:
        start_new_order(message_from_user, user)
        return answer.get(message_from_user, error)
    else:
        return answer.get(message_from_user, error)


def command_order_process(message_from_user, user):
    if check_keyboard_command(message_from_user) is True:
        if check_cancel_order(message_from_user) is True:
            cancel_order(message_from_user, user)
            return answer.get(message_from_user)
        else:
            return incorrect_command
    else:
        db_functions.check_order_step


def send_message_choice(message_from_user, user):
    if db_functions.check_opened_orders(user) is True:
        return command_order_process(message_from_user, user)
    else:
        return command_before_order(message_from_user, user)


def answer_to_user(message_from_user, user=None, show_keyboard=None):
    show_keyboard = keyboard_choice(message_from_user)
    send_message = send_message_choice(message_from_user, user)
    logging_rules.write_outcoming(send_message_choice(message_from_user, user), user)
    VKMethods.send_msg('user_id', user, send_message, show_keyboard)
