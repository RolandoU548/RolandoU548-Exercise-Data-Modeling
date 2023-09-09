import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    full_name = Column(String(250), nullable=False)
    user_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)

    def log_in():
        print("Logged In")

    def sign_in():
        print("Signed In")

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250) , nullable=False)
    size = Column(String(250) , nullable=False)
    population = Column(Integer)

class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250) , nullable=False)
    hair_color = Column(String(250))
    eye_color = Column(String(250))
    height = Column(Integer, nullable = False)
    age = Column(Integer, nullable = False)

class Vehicles(Base):
    __tablename__ = 'vehicles'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    model = Column(String(250) , nullable=False)
    manufacturer = Column(String(250) , nullable = False)
    capacity = Column(Integer)
    speed = Column(Integer, nullable = False)
    weight = Column(Integer, nullable = False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    users = relationship(Users)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planets = relationship(Planets)
    character_id = Column(Integer, ForeignKey('character.id'))
    characters = relationship(Characters)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicles = relationship(Vehicles)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
