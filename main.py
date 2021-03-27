import get_vk
from vk_api.bot_longpoll import VkBotEventType
import logging_rules
import messages


longpoll = get_vk.Bot_longpoll()


while True:
    try:
        for event in longpoll.listen():
            if event.type == VkBotEventType.MESSAGE_NEW:
                message_from_user = event.obj.text
                logging_rules.write_incoming(event.obj.text, event.obj.from_id)
                if event.from_user:
                    messages.answer_to_user(message_from_user,
                                            event.obj.from_id)
    except (KeyboardInterrupt, SystemExit):
        raise
    except Exception:
        logging_rules.write_log_exception("Catched an exception")
        raise
