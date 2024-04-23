import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):

    __tablename__ ='users'
    id_users =Column(Integer, primary_key= True)
    user_name =Column(String(250))
    user_lastName = Column(String(250))
    user_email = Column(String(200))
    user_gender = Column(String(20))
    user_password = Column(String(20))
    user_fecha_suscripcion =Column (Date, nullable=False)
    id_favorites =Column(Integer, ForeignKey('favorites.id_favorites'))
    
    

class Favorites (Base):
    __tablename__='favorites'
    id_favorites = Column(Integer, primary_key = True)
    id_users = Column(Integer, ForeignKey('users.id_users'))
    id_planets = Column(Integer, ForeignKey('planets.id_planets'))
    id_characters = Column(Integer, ForeignKey('characters.id_characters'))
    id_vehicles = Column(Integer, ForeignKey('vehicles.id_vehicles'))
    

class Planets(Base):

    __tablename__ = 'Planets'
    id_planets = Column(Integer, primary_key = True)
    planets_name= Column(String(100))
    planets_terrain =Column(String(100))
    planets_description =Column(String(300))
    id_favorites = Column(Integer, ForeignKey('favorites.id_favorites'))
    favorites = relationship(Favorites)


class Vehicles(Base):

    __tablename__ = 'Vehicles'
    id_vehicles = Column(Integer, primary_key = True)
    vehicles_name= Column(String(100))
    vehicles_description =Column(String(300))
    id_favorites = Column(Integer, ForeignKey('favorites.id_favorites'))
    favorites = relationship(Favorites)

class Characters(Base):

    __tablename__ = 'Characters'
    id_characters = Column(Integer, primary_key = True)
    characters_name= Column(String(100))
    characters_type= Column(String(50))
    characters_description =Column(String(300))
    id_favorites = Column(Integer, ForeignKey('favorites.id_favorites'))
    id_creatures = Column(Integer, ForeignKey('creatures.id_creatures'))
    id_droids = Column(Integer, ForeignKey('droids.id_droids'))
    favorites = relationship(Favorites)

class Creatures(Base):
    __tablename__ = 'creatures'

    id_creatures =(Column(Integer, primary_key =True))
    creatures_name =(Column(String(50)))
    creatures_description =Column(String(300))
    d_characters = Column(Integer, ForeignKey('characters.id_characters'))
    Characters = relationship(Characters)

class Droids(Base):
    __tablename__ ='droids'
    id_droids =(Column(Integer, primary_key =True))
    droids_name =(Column(String(50)))
    droids_description =Column(String(300))
    id_characters = Column(Integer, ForeignKey('characters.id_characters'))
    Characters = relationship(Characters)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
