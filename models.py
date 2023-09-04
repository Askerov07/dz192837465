#   ФАБРИКА асинхронных движков и асинхронных сессий
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

from db_conf import DSN
engine = create_async_engine(DSN)

# менеджер сессий
from sqlalchemy.orm import sessionmaker

# базовый класс для сессий (ФАБРИКА СЕССИЙ)
Session = sessionmaker(bind=engine,
                       class_=AsyncSession,
                       expire_on_commit=False
                       )

# ФАБРИКА базовых классов
from sqlalchemy.ext.declarative import declarative_base

# базовый класс для моделей
Base = declarative_base()

from sqlalchemy import Column, Integer, String, ARRAY


# модель персонажей
class SwapiPeople(Base):
    __tablename__ = 'swapi_people'

    id = Column(Integer, primary_key=True, autoincrement=False)
    birth_year = Column(String(50))
    eye_color = Column(String(50))
    films = Column(ARRAY(String))       # Список
    gender = Column(String(50))
    hair_color = Column(String(50))
    height = Column(String(50))
    homeworld = Column(String(50))
    mass = Column(String(50))
    name = Column(String(50))
    skin_color = Column(String(50))
    species = Column(ARRAY(String))     # Список
    starships = Column(ARRAY(String))   # Список
    vehicles = Column(ARRAY(String))    # Список
