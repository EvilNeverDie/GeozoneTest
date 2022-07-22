from geoalchemy2 import Geometry, Geography
from sqlalchemy import Column, Integer, String

from database import Base


class Geozone(Base):
    __tablename__ = 'geozone'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    geom = Column(Geography('POLYGON'))
