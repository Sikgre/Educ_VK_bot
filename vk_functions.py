from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from vk_api.utils import get_random_id
import settings


class VKMethods():
    session = VkApi(token=settings.token)

    @classmethod
    def Bot_longpoll(cls):
        return VkBotLongPoll(VKMethods.session, settings.group_id, wait=60)

    @classmethod
    def get_user(cls, user_id):
        user_info = cls.session.method('users.get', {'user_ids': user_id})
        return user_info

    @classmethod
    def send_msg(cls, id_type, id, msg_to_user,
                 keyboard=None, attachment=None):
        cls.session.method('messages.send',
                           {id_type: id,
                            'message': msg_to_user(),
                            'random_id': get_random_id(),
                            'keyboard': keyboard()
                            }
                           )
