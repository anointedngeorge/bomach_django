

from ninja import Router
from settings.submodels.model_gallery import *
from admin.schemas.schema_gallery import *
from django.shortcuts import get_object_or_404
from typing import List

router = Router(tags=["Gallery"])


@router.post('/register-gallery/')
def register_image_gallery(request, id:int):
    '''
    Register image gallery...
    '''
    return {"message":"Register image API interface"}



# @api.get("/employees/{employee_id}", response=EmployeeOut)
# def get_employee(request, employee_id: int):
#     employee = get_object_or_404(Employee, id=employee_id)
#     return employee


@router.get('/get-gallery-image/', response=List[GalleryOut])
def get_gallery_image(request):
    '''Get gallery image'''
    gallery = Gallery.objects.all()
    return gallery



@router.put('/update-gallery{id}/')
def update_image_gallery(request, id:int):
    '''
    Updating image api...
    '''
    return {"message":"Image API interface"}
