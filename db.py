from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
import settings

engine = create_engine(settings.db_connection)
db_session = scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

# написать функцию добавления пользователя и поставить её во всех функции,
# которыми пользователь пользуется
# протестировать
