import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Filament(SqlAlchemyBase):
    __tablename__ = 'filament'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    filament = sqlalchemy.Column(sqlalchemy.String, nullable=True)