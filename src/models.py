import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)
    

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_diameter = Column(Integer)
    planet_terrain = Column(String(250))
    planet_name = Column(String(250), nullable=False)
    fav_planets = relationship('Fav_planets', backref='user', lazy=True)


class Characters(Base):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    characters_mass = Column(Integer)
    characters_gender = Column(String(250))
    characters_name = Column(String(250), nullable=False)
    fav_characters = relationship('Fav_characters', backref='user', lazy=True)

class Fav_planets(Base):
    __tablename__ = 'fav_planets'
    id = Column (Integer,primary_key=True)
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer,ForeignKey('user.id'))
    planets_id = Column(Integer,ForeignKey('planets.id'))

    
class Fav_characters(Base):
    __tablename__ = 'fav_characters'
    id = Column (Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('user.id'))
    charaters_id = Column(Integer,ForeignKey('characters.id'))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
