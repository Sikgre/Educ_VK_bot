from db import db_session
from models import User


def new_user(user_vk_id):
    return bool(User.query.filter(User.user_vk_id == user_vk_id).count())


def add_user(user_vk_id, user_name):
    user = User(user_vk_id=user_vk_id, user_name=user_name)
    if new_user(user_vk_id) is False:
        db_session.add(user)
        db_session.commit()
