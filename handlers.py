import json
import logging_rules
from messages import answer, keyboard_command, steps
from keyboard import keyboard_choice, keyboard_empty
from vk_functions import VKMethods
from db_functions import check_DB, get_DB, Upsert_DB, Bot_status
from db_models import Order
from settings import admin_id


class CheckConditions():

    @staticmethod
    def check_keyboard_command(message_from_user):
        return bool(message_from_user in keyboard_command.values())

    @staticmethod
    def check_cancel_order(message_from_user):
        return bool(message_from_user == keyboard_command["cancel"])

    @staticmethod
    def check_create_order(message_from_user):
        return bool(message_from_user == keyboard_command["document"]
                    or
                    message_from_user == keyboard_command["consulting"])


class OrderCommands():

    @staticmethod
    def start_new_order(message_from_user, user):
        if message_from_user == keyboard_command["document"]:
            Upsert_DB.add_order_document(user)
        elif message_from_user == keyboard_command["consulting"]:
            Upsert_DB.add_order_consulting(user)

    @staticmethod
    def cancel_order(message_from_user, user):
        if CheckConditions.check_cancel_order(message_from_user) is True:
            Upsert_DB.cancel_order(user)


class MessageHandler():

    @classmethod
    def command_before_order(cls, message_from_user, user):
        if CheckConditions.check_create_order(message_from_user) is True:
            OrderCommands.start_new_order(message_from_user, user)
            return answer.get(message_from_user, answer["unknown_command"])
        else:
            return answer.get(message_from_user, answer["unknown_command"])

    @classmethod
    def command_order_process(cls, message_from_user, user):
        if CheckConditions.check_keyboard_command(message_from_user) is True:
            if CheckConditions.check_cancel_order(message_from_user) is True:
                OrderCommands.cancel_order(message_from_user, user)
                return answer.get(message_from_user)
            else:
                return answer.get("incorrect_command")
        else:
            return cls.order_processing(message_from_user, user)

    @classmethod
    def send_message_choice(cls, message_from_user, user):
        if check_DB.check_opened_orders(user) is True:
            return cls.command_order_process(message_from_user, user)
        else:
            return cls.command_before_order(message_from_user, user)

    @classmethod
    def order_processing(cls, message_from_user, user):
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
        description = check_DB.check_empty_description(user)
        if description is False:
            order_type = get_DB.get_order_type(user)
            parameters = order_parameters[order_type]
            parameters["type"] = message_from_user
            final_parameters = json.dumps(parameters)
            message_to_user = steps[order_type]["type"]
            Upsert_DB.add_order_description(user, final_parameters)
            return message_to_user
        else:
            parameters = json.loads(get_DB.get_order_description(user))
            if bool(list(parameters.values()).count(None)) is True:
                order_type = get_DB.get_order_type(user)
                for i in parameters:
                    if parameters[i] is None:
                        parameters[i] = message_from_user
                        message_to_user = steps[order_type][i]
                        final_parameters = json.dumps(parameters)
                        Upsert_DB.add_order_description(user, final_parameters)
                        return message_to_user
                        break
            else:
                if check_DB.check_order_comments(user) is False:
                    Upsert_DB.add_order_comments(user, message_from_user)
                    message_to_user = steps["comments"]
                    return message_to_user
                else:
                    message_to_user = steps["finish_order"]
                    Upsert_DB.finish_order(user)
                    print("Закрыли заказ")
                    if check_DB.check_correct_order(user) is True:
                        Upsert_DB.sended_mark_on(user)
                        print("Поставили отметку о закрытии")
                        Bot_status.turn_off(user)
                        cls.send_to_admin(user)
                        return message_to_user

    @classmethod
    def answer_to_user(cls, message_from_user, user=None, show_keyboard=None):
        send_message = cls.send_message_choice(message_from_user, user)
        try:
            show_keyboard = keyboard_choice(send_message)
        except TypeError:
            show_keyboard = keyboard_empty
        logging_rules.write_outcoming(send_message, user)
        VKMethods.send_msg('user_id', user, send_message, show_keyboard)

    @classmethod
    def send_to_admin(cls, user):
        order_id = get_DB.get_last_order(user)
        order = Order.query.filter(Order.id == order_id).first()
        description = order.description
        VKMethods.send_msg('user_id', admin_id, description, keyboard_empty)
