from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from datetime import datetime
import random
import settings


vk_session = VkApi(token = settings.token)
session_api = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, settings.group_id)

while True:
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(f'Сообщение пришло в: {str(datetime.strftime(datetime.now(), "%d.%m %H:%M:%S"))}')
            print(f'Текст сообщения: {event.obj.text}')
            print(f'ID пользователя: {event.obj.from_id}')
            message = event.obj.text
            if event.from_user:
                vk_session.method('messages.send', {'user_id': event.obj.from_id, 'message': message, 'random_id': random.randint(-2147483648, +2147483648)})

