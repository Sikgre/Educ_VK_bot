import logging
from datetime import datetime


logging.basicConfig(filename="logs.log", level=logging.DEBUG)

now = str(datetime.strftime(datetime.now(), "%d.%m %H:%M:%S"))


def log_incoming_msg(message, user):
    return (f'Входящее сообщение. Дата: {now}, \n'
            f'сообщение: {message}, \n ID пользователя: {user} \n')


def log_outcoming_msg(message, user):
    return (f'Исходящее сообщение. Дата: {now}, \n'
            f'сообщение: {message}, \n ID пользователя: {user} \n')


def write_incoming(message, user):
    return logging.info(log_incoming_msg(message, user))


def write_outcoming(message, user):
    return logging.info(log_outcoming_msg(message, user))


def write_log_exception(text):
    return logging.exception(text)
