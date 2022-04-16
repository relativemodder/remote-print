import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Data(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    way = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    filament_type = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    color = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)

