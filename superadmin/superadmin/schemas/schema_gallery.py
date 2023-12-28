from datetime import date
from ninja import Schema



class GalleryIn(Schema):
    name: str


class GalleryOut(Schema):
    id:int
    name:str
    size:int
    filename:str
    data:str