from sqlalchemy import Column, Integer, String, DateTime, JSON, Boolean
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    vk_id = Column(Integer, unique=True)
    name = Column(String)
    bot_off = Column(Boolean, default=False)

    def __init__(self, vk_id, name):
        self.vk_id = vk_id
        self.name = name

    def __repr__(self):
        return f'<User vk_id:{self.vk_id}, name: {self.name}>'


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String)
    order_type = Column(String)
    user_id = Column(Integer, ForeignKey(User.id))
    description = Column(JSON)
    comments = Column(String)
    sended = Column(Boolean, default=False)

    user = relationship(User, backref="orders")

    def __init__(self, status, order_type, user_id):
        self.status = status
        self.order_type = order_type
        self.user_id = user_id

    def __repr__(self):
        return
        f'<Order: {self.id}, type: {self.order_type}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
