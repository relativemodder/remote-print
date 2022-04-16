import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Color(SqlAlchemyBase):
    __tablename__ = 'color'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    color = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    data = orm.relation("Data", back_populates='color')