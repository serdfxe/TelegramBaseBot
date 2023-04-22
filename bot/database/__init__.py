from sqlalchemy.engine import create_engine

from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

import bot.config as conf


engine = create_engine(conf.DATABASE_URL)

Base = declarative_base()

Session = sessionmaker(bind=engine)


def get_session():
    print("New Session!")
    return Session()
