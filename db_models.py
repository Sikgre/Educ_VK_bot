from sqlalchemy import Column, Integer, String, Enum, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    vk_id = Column(Integer, unique=True)
    name = Column(String)

    def __init__(self, vk_id, name):
        self.vk_id = vk_id
        self.name = name

    def __repr__(self):
        return f'<User vk_id:{self.vk_id}, name: {self.name}>'


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum("opened", "closed", "cancelled", name="statuses"))
    order_type = Column(Enum("document", "consulting", name="order_types"))
    user_id = Column(Integer, ForeignKey(User.id))
    deadline = Column(String)
    description = Column(String)

    user = relationship(User, backref="orders")

    def __init__(self, status, order_type, user_id,
                 deadline, description):
        self.status = status
        self.order_type = order_type
        self.user_id = user_id
        self.deadline = deadline
        self.description = description

    def __repr__(self):
        return
        f'<Order: {self.id}, type: {self.type_id}, '
        f'deadline: {self.deadline}, '
        f'description: {self.description}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
