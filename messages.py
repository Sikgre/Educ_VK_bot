import json
import logging_rules
from handlers import answer, keyboard_command, steps
from keyboard import keyboard_choice, keyboard_empty
from vk_functions import VKMethods
import db_functions


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
        return answer.get(message_from_user, answer["unknown_command"])
    else:
        return answer.get(message_from_user, answer["unknown_command"])


def command_order_process(message_from_user, user):
    if check_keyboard_command(message_from_user) is True:
        if check_cancel_order(message_from_user) is True:
            cancel_order(message_from_user, user)
            return answer.get(message_from_user)
        else:
            return answer.get("incorrect_command")
    else:
        return order_processing(message_from_user, user)


def send_message_choice(message_from_user, user):
    if db_functions.check_opened_orders(user) is True:
        return command_order_process(message_from_user, user)
    else:
        return command_before_order(message_from_user, user)


def order_processing(message_from_user, user):
    order_parameters = {
        "document":
            {
                "type": None,
                "file_1": None,
                "file_2": None
            },
        "consulting":
            {
                "type": None,
                "your_question": None
            }
        }
    description = db_functions.check_empty_description(user)
    if description is False:
        order_type = db_functions.get_order_type(user)
        parameters = order_parameters[order_type]
        parameters["type"] = message_from_user
        final_parameters = json.dumps(parameters)
        message_to_user = steps[order_type]["type"]
        db_functions.add_order_description(user, final_parameters)
        return message_to_user
    else:
        parameters = json.loads(db_functions.get_order_description(user))
        if bool(list(parameters.values()).count(None)) is True:
            order_type = db_functions.get_order_type(user)
            for i in parameters:
                if parameters[i] is None:
                    parameters[i] = message_from_user
                    message_to_user = steps[order_type][i]
                    final_parameters = json.dumps(parameters)
                    db_functions.add_order_description(user, final_parameters)
                    return message_to_user
                    break
        else:
            message_to_user = steps["finish_order"]
            db_functions.finish_order(user)
            return message_to_user


def answer_to_user(message_from_user, user=None, show_keyboard=None):
    send_message = send_message_choice(message_from_user, user)
    try:
        show_keyboard = keyboard_choice(send_message)
    except TypeError:
        show_keyboard = keyboard_empty
    logging_rules.write_outcoming(send_message, user)
    VKMethods.send_msg('user_id', user, send_message, show_keyboard)
