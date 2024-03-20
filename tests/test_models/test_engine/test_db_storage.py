#!/usr/bin/python3
"""
    tests for FileStorage
"""
import unittest
from models.base_model import BaseModel
from sqlalchemy.engine.base import Engine
from datetime import datetime
from models.engine import db_storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import os
from models import storage
from models.user import User
import pycodestyle

@unittest.skipIf(
    os.getenv('HBNB_TYPE_STORAGE') != 'db', 'DBStorage test')

class test_DBStorage(unittest.TestCase):
    """
        Base test class
    """
    @classmethod
    def setUpClass(cls):
        """
            setup
        """
        cls.dummy = DBStorage()

        @classmethod
    def tearDownClass(cls):
        """
            tear down
        """
        del cls.dummy

    def test_attrs(self):
        """
            attribute tests
        """
        self.assertTrue(hasattr(self.dummy, '_DBStorage__engine'))
        self.assertTrue(hasattr(self.dummy, '_DBStorage__session'))
        self.assertTrue(isinstance(self.dummy._DBStorage__engine, Engine))
        self.assertTrue(self.dummy._DBStorage__session is None)

if __name__ == "__main__":
    unittest.main()