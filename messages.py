import json
import logging_rules
import get_vk
import handlers
import keyboard

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


def answer_to_user(message_from_user, user=None, show_keyboard=None):
    answer = handlers.keyboard_functions
    show_keyboard = keyboard.keyboard_choice(message_from_user)
    send_message = answer.get(message_from_user, 'No such key in keyboard_functions')
    logging_rules.write_outcoming(send_message, user)
    return get_vk.send_msg('user_id', user, send_message, show_keyboard)
    # else:
    #     keyboard = keyboard.keyboard_begin
    #     send_message = buttons_and_messages.error_messages["unknown_command"]
    #     logging_rules.write_outcoming(send_message, user)
    #     return get_vk.send_msg('user_id', user, send_message, keyboard)
