#!/usr/bin/python3

"""New engine for the databas"""
import os
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBStorage:

    """New database engine for our Hbnb Project
    to connect to Mysql
    """

    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database"""
        from urllib.parse import quote_plus

        # get the system environmen variables

        usr = os.getenv(HBNB_MYSQL_USER)
        passwd = quote_plus(os.getenv(HBNB_MYSQL_PWD))
        host = os.getenv(HBNB_MYSQL_HOST)
        db = os.getenv(HBNB_MYSQL_DB)
        env = os.getenv(HBNB_ENV)

        # connect to the database engine
        uri = f"mysql+mysqldb//:{usr}@{host}:3306/{db}"


        self.__engine = create_engine(uri, pool_pre_ping=True)
        Session = sessionmaker(bind=engine)
        DBStorage.__session = Session()

        # delete the test.* if env is "test"
        if env == "test":
            Base.metadata.drop_all(engine)

        # Base.metadata.create_all(engine)


    def all(self, cls=None):
        """
        Queries the current database"""

        table_names = [
                "User",
                "State",
                "city",
                "Amenity",
                "Place",
                "Review"
        ]
        """
        classes = {
                "User": User,
                "BaseModel": BaseModel,
                "City": City,
                "Amenity": Amenity,
                "State": State,
                "Place": Place,
                "Review": Review
        }
        """

        dictionary = {}
        if cls is None:
            
            # query the database tables
            for name in table_names:
                result = DBStorage.__session.query(name).all()

                # loop through the objects and store in our local dict
                for obj in result:
                    key = obj.to_dict()['__class__'] + "." + obj.id
                    dictionary[key] = obj
        else:
            result = DBStorage.__session.query(str(cls)).all()

            for obj in result:
                key = obj.to_dict()['__class__'] + '.' + obj.id
                dictionary[key] = obj


    def new(self, obj):
        """Adds a new object to the current database session"""

        DBStorage.__session.add(obj)


    def save(self):
        """Commits all changes of the current database session"""
        DBStorage.__session.commit()


    def delete(self, obj=None):
        """Deletes from a current database session"""
        if obj:
            DBStorage.__session.delete(obj)
            # DBStorage.__session.commit()

    def reload(self):
        """Creates all tables in the database"""



        pass

