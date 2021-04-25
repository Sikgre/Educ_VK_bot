from db import db_session
from db_models import User, Order
from logging_rules import log_exception_text


class check_DB():

    @staticmethod
    def check_new_user(vk_id):
        return bool(User.query.filter(User.vk_id == vk_id).count())

    @staticmethod
    def check_opened_orders(vk_id):
        user_id = get_DB.get_user_id(vk_id)
        opened_orders = Order.query.filter(
            Order.user_id == user_id,
            Order.status == 'opened'
            ).count()
        return bool(opened_orders)

    @staticmethod
    def check_empty_description(vk_id):
        order_id = get_DB.get_opened_order(vk_id)
        if order_id is not None:
            order = Order.query.filter(Order.id == order_id).first()
            return bool(order.description)

    @staticmethod
    def check_order_comments(vk_id):
        order_id = get_DB.get_opened_order(vk_id)
        order = Order.query.filter(Order.id == order_id).first()
        return bool(order.comments)

    @staticmethod
    def check_correct_order(vk_id):
        order_id = get_DB.get_last_order(vk_id)
        order = Order.query.filter(Order.id == order_id).first()
        if ((order.comments is not None) and
           (order.description is not None) and
           (order.sended is False) and
           order.status == "finished"):
            return True

    @staticmethod
    def check_bot_off(vk_id):
        user_id = get_DB.get_user_id(vk_id)
        user = User.query.filter(User.id == user_id).first()
        return user.bot_off


class get_DB():

    @staticmethod
    def get_user_id(vk_id):
        user = User.query.filter(User.vk_id == vk_id).first()
        return user.id

    @classmethod
    def get_opened_order(cls, vk_id):
        try:
            user_id = cls.get_user_id(vk_id)
            order = Order.query.filter(
                Order.user_id == user_id,
                Order.status == 'opened'
                ).first()
            return order.id
        except AttributeError:
            log_exception_text(
                'Вызвана команда получения открытых заказов.'
                'Открытых заказов не найдено')

    @classmethod
    def get_order_type(cls, vk_id):
        order_id = cls.get_opened_order(vk_id)
        order = Order.query.filter(Order.id == order_id).first()
        return order.order_type

    @classmethod
    def get_order_description(cls, vk_id):
        order_id = cls.get_opened_order(vk_id)
        order = Order.query.filter(Order.id == order_id).first()
        return order.description

    @classmethod
    def get_last_order(cls, vk_id):
        user_id = cls.get_user_id(vk_id)
        order = Order.query.filter(
            Order.user_id == user_id
            ).order_by(Order.created_at.desc()).first()
        return order.id


class Upsert_DB():

    @staticmethod
    def add_user(vk_id, name):
        user = User(vk_id=vk_id, name=name)
        if check_DB.check_new_user(vk_id) is False:
            db_session.add(user)
            db_session.commit()

    @staticmethod
    def add_order_document(vk_id):
        user_id = get_DB.get_user_id(vk_id)
        order = Order(status="opened", order_type="document", user_id=user_id)
        db_session.add(order)
        db_session.commit()

    @staticmethod
    def add_order_consulting(vk_id):
        user_id = get_DB.get_user_id(vk_id)
        order = Order(status="opened", order_type="consulting", user_id=user_id)
        db_session.add(order)
        db_session.commit()

    @staticmethod
    def add_order_description(vk_id, description):
        order_id = get_DB.get_opened_order(vk_id)
        Order.query.filter(Order.id == order_id).update({
            Order.description: description}, synchronize_session=False)
        db_session.commit()

    @staticmethod
    def add_order_comments(vk_id, comments):
        order_id = get_DB.get_opened_order(vk_id)
        Order.query.filter(Order.id == order_id).update({
            Order.comments: comments}, synchronize_session=False)
        db_session.commit()

    @staticmethod
    def cancel_order(vk_id):
        order_id = get_DB.get_opened_order(vk_id)
        Order.query.filter(Order.id == order_id).update({
            Order.status: "cancelled"}, synchronize_session=False)
        db_session.commit()

    @staticmethod
    def finish_order(vk_id):
        order_id = get_DB.get_opened_order(vk_id)
        Order.query.filter(Order.id == order_id).update({
            Order.status: "finished"}, synchronize_session=False)
        db_session.commit()

    @staticmethod
    def sended_mark_on(vk_id):
        order_id = get_DB.get_last_order(vk_id)
        Order.query.filter(Order.id == order_id).update({
            Order.sended: True}, synchronize_session=False)
        db_session.commit()


class Bot_status():

    @staticmethod
    def turn_off(vk_id):
        order_id = get_DB.get_last_order(vk_id)
        order = Order.query.filter(Order.id == order_id).first()
        if order.status == 'finished' and order.sended is True:
            user_id = get_DB.get_user_id(vk_id)
            User.query.filter(User.id == user_id).update({
                            User.bot_off: True}, synchronize_session=False)
            db_session.commit()

    @staticmethod
    def turn_on(message_from_user, vk_id):
        user_id = get_DB.get_user_id(vk_id)
        if message_from_user == 'Включить бота':
            User.query.filter(User.id == user_id).update({
                            User.bot_off: False}, synchronize_session=False)
            db_session.commit()
