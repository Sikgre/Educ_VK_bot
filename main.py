from vk_api.bot_longpoll import VkBotEventType
import logging_rules
from handlers import MessageHandler
from db_functions import Upsert_DB
import requests
from vk_functions import VKMethods


longpoll = VKMethods.Bot_longpoll()


'''
Цикл прослушивания сообщений с сервера ВК и их обработки.
При получении нового сообщения запускается функция ответа,
определённая в messages.py
'''

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_user:
                    message_from_user = event.obj.text
                    user = VKMethods.get_user(event.obj.from_id)
                    user_name = user[0]['first_name'] + ' ' + user[0]['last_name']
                    Upsert_DB.add_user(event.obj.from_id, user_name)
                    logging_rules.write_incoming(message_from_user,
                                                 event.obj.from_id)
                    MessageHandler.answer_to_user(message_from_user,
                                                  event.obj.from_id)
    except (KeyboardInterrupt, SystemExit):
        raise
    except requests.exceptions.ReadTimeout:
        continue
    except Exception:
        logging_rules.write_log_exception("Catched an exception")
        raise
