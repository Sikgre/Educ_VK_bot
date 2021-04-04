from db import db_session
from models import User


def new_user(user_vk_id):
    user = User.query.filter(User.user_vk_id == user_vk_id)
    number = 0
    for i in user:
        number += 1
    if number >= 1:
        return False
    else:
        return True


def add_user(user_vk_id, user_name):
    user = User(user_vk_id=user_vk_id, user_name=user_name)
    if new_user(user_vk_id) is True:
        db_session.add(user)
        db_session.commit()
    else:
        pass
