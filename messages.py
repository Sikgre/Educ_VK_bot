
import json
import buttons_and_messages
import logging_rules
import get_vk
import keyboard


def write_message(obj):
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(obj))


def answer_to_user(message_from_user, user=None, show_keyboard=None):
    dict_message = buttons_and_messages.answer_command(message_from_user)
    choice_key = str(list(dict_message.keys())[0])
    send_message = dict_message[choice_key]
    show_keyboard = keyboard.keyboard_choice(message_from_user)
    logging_rules.write_outcoming(send_message, user)
    return get_vk.send_msg('user_id', user, send_message, show_keyboard)
    # else:
    #     keyboard = keyboard.keyboard_begin
    #     send_message = buttons_and_messages.error_messages["unknown_command"]
    #     logging_rules.write_outcoming(send_message, user)
    #     return get_vk.send_msg('user_id', user, send_message, keyboard)