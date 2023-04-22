from sqlalchemy import Column, BigInteger, String, Boolean

from bot.database import Base

from bot.database.db_tool import DBTool


class User(Base, DBTool):
    __tablename__ = 'users'
    
    id = Column(BigInteger, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    role = Column(String)
    banned = Column(Boolean)
