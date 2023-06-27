from typing import TYPE_CHECKING

from sqlalchemy import Column, Integer, String, Enum

from .database import db

if TYPE_CHECKING:
    from flask_sqlalchemy.query import Query


class Users(db.Model):
    id = Column(Integer, primary_key=True)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(Enum("female", "male", name="gender", create_type=False, nullable=False))

    if TYPE_CHECKING:
        query: Query
