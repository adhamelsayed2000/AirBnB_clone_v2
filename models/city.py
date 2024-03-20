from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """ City class """
    __tablename__ = "cities"

    places = relationship("Place", cascade="all, delete", backref="cities")