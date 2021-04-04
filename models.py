from sqlalchemy import Column, Integer, String
from db import Base, engine


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_vk_id = Column(Integer, unique=True)
    user_name = Column(String)

    def __repr__(self):
        return f'<User {self.user_vk_id} {self.user_name}>'


if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
