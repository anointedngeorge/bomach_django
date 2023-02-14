from datetime import date
from ninja import Schema



class GalleryIn(Schema):
    first_name: str
    last_name: str
    department_id: int = None
    birthdate: date = None


class GalleryOut(Schema):
    id:int
    filesize:str
    name:str
    url:str
    size:int
    filename:str