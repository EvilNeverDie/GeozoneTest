from typing import List

from pydantic import BaseModel


class Coord(BaseModel):
    lat: float
    lng: float


class GeozoneCreate(BaseModel):
    name: str
    geom: List[Coord]

    def dict(self, *args, **kwargs):
        result = {"name": self.name}
        geom = f'POLYGON(({",".join([f"{i.lat} {i.lng}" for i in self.geom])}))'
        result['geom'] = geom
        return result

