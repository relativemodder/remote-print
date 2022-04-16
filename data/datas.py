import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Data(SqlAlchemyBase):
    __tablename__ = 'data'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    way = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    filament_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("filament.id"))
    color_type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("colors.id"))
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    filament = orm.relation('Filament')
    color = orm.relation('Color')
    user = orm.relation('User')



