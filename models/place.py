#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship



metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
        Column("place_id", String(60), ForeignKey("places.id"), primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"), primary_key=True, nullable=False)
)



class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=int(0))
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        "If database is connected"
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary=place_amenity, viewonly=False)
    else:
        from models import storage

        @property
        def reviews(self):

            all_objects = storage.all(Review)

            reviews = []
            for k, v in all_objects:

                if (
                    v.to_dict()["__class__"] == "Review"
                    and self.id == v.to_dict()["place_id"]
                ):
                    reviews.append(v)
            return reviews

        @property
        def amenities(self):

            all_objects = storage.all(Amenity)

            for a_id in amenity_ids:
                for k, v in all_objects:
                    if a_id == v.to_dict()['id']:
                        amenities.append(v)
                        break

        @amenities.setter
        def amenities(self, value):

            if isinstance(value, Amenity):
                amenity_ids.append(value.to_dict()['id'])

