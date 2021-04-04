import settings
from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id

session = VkApi(token=settings.token)
session_api = session.get_api()

'''
Здесь перечислены все функции, использующие методы API ВК
'''


def Bot_longpoll():
    return VkBotLongPoll(session, settings.group_id, wait=60)


def get_user(user_id):
    user_info = session.method('users.get', {'user_ids': user_id})
    return user_info


def send_msg(id_type, id, msg_to_user, keyboard=None, attachment=None):
    session.method('messages.send',
                   {id_type: id, 'message': msg_to_user,
                    'random_id': get_random_id(),
                    'keyboard': keyboard})


def new_user(user_id):
    get_conversations = session.method(
        'messages.getConversationsById',
        {'peer_ids': user_id, 'group_id': int(settings.group_id)}
        )
    number_of_messages = get_conversations["items"][0]["last_message_id"]
    if number_of_messages > 1:
        print(number_of_messages)
        return False
    else:
        return True
