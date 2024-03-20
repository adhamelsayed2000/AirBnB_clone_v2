from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """ User class """
    __tablename__ = "users"

    places = relationship("Place", cascade="all, delete", backref="user")
