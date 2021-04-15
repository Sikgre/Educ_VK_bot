from db import db_session
from db_models import User, Order
from logging_rules import log_exception_text


def check_new_user(vk_id):
    return bool(User.query.filter(User.vk_id == vk_id).count())


def add_user(vk_id, name):
    user = User(vk_id=vk_id, name=name)
    if check_new_user(vk_id) is False:
        db_session.add(user)
        db_session.commit()


def get_user_id(vk_id):
    user = User.query.filter(User.vk_id == vk_id).first()
    return user.id


def check_opened_orders(vk_id):
    user_id = get_user_id(vk_id)
    opened_orders = Order.query.filter(
        Order.user_id == user_id,
        Order.status == 'opened'
        ).count()
    return bool(opened_orders)


def add_order_document(vk_id):
    user_id = get_user_id(vk_id)
    order = Order(status="opened", order_type="document", user_id=user_id)
    db_session.add(order)
    db_session.commit()


def add_order_consulting(vk_id):
    user_id = get_user_id(vk_id)
    order = Order(status="opened", order_type="consulting", user_id=user_id)
    db_session.add(order)
    db_session.commit()


def get_opened_order(vk_id):
    try:
        user_id = get_user_id(vk_id)
        order = Order.query.filter(
            Order.user_id == user_id,
            Order.status == 'opened'
            ).first()
        return order.id
    except AttributeError:
        log_exception_text(
            'Вызвана команда получения открытых заказов.'
            'Открытых заказов не найдено')


def get_order_type(vk_id):
    order_id = get_opened_order(vk_id)
    order = Order.query.filter(Order.id == order_id).first()
    return order.order_type


def cancel_order(vk_id):
    order_id = get_opened_order(vk_id)
    Order.query.filter(Order.id == order_id).update({
        Order.status: "cancelled"}, synchronize_session=False)
    db_session.commit()


def check_empty_description(vk_id):
    order_id = get_opened_order(vk_id)
    if order_id is not None:
        order = Order.query.filter(Order.id == order_id).first()
        return bool(order.description)


def add_order_description(vk_id, description):
    order_id = get_opened_order(vk_id)
    Order.query.filter(Order.id == order_id).update({
        Order.description: description}, synchronize_session=False)
    db_session.commit()


def get_order_description(vk_id):
    order_id = get_opened_order(vk_id)
    order = Order.query.filter(Order.id == order_id).first()
    return order.description


def finish_order(vk_id):
    order_id = get_opened_order(vk_id)
    Order.query.filter(Order.id == order_id).update({
        Order.status: "finished"}, synchronize_session=False)
    db_session.commit()
