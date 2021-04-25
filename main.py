from vk_api.bot_longpoll import VkBotEventType
import logging_rules
from handlers import MessageHandler
from db_functions import Upsert_DB, check_DB, Bot_status
import requests
from vk_functions import VKMethods
from settings import admin_id


longpoll = VKMethods.Bot_longpoll()

while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                if event.from_user:
                    message_from_user = event.obj.text
                    vk_id = event.obj.from_id
                    user = VKMethods.get_user(vk_id)
                    user_name = user[0]['first_name'] + ' ' + user[0]['last_name']
                    Upsert_DB.add_user(vk_id, user_name)
                    logging_rules.write_incoming(message_from_user, vk_id)
                    bot_off = check_DB.check_bot_off(vk_id)
                    if bot_off is False:
                        MessageHandler.answer_to_user(message_from_user, vk_id)
                    else:
                        Bot_status.turn_on(message_from_user, vk_id)
            elif event.type == VkBotEventType.MESSAGE_REPLY:
                if event.obj.peer_id != int(admin_id):
                    Bot_status.turn_on(event.obj.text, event.obj.peer_id)
    except (KeyboardInterrupt, SystemExit):
        raise
    except requests.exceptions.ReadTimeout:
        continue
    except Exception:
        logging_rules.write_log_exception("Catched an exception")
        raise
