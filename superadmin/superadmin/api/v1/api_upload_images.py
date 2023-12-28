

from ninja import Router
from settings.submodels.model_gallery import *
from superadmin.schemas.schema_gallery import *
from django.shortcuts import get_object_or_404
from typing import List
from ninja import NinjaAPI, File
from ninja.files import UploadedFile
import pickle
import os
import sys
import base64

router = Router(tags=["Gallery"])


filename =  '/admin/admin/image_pickled.txt'
image_filename = '/admin/images/'


@router.post('/register-gallery/')
def register_image_gallery(request, filename:str, file: UploadedFile = File(...)):
    filedata = file.read()
    # print(name)
    encode =  base64.encodebytes(filedata)
    g=Gallery.objects.all()
    data = {
        'name':filename,
        'size':file.size,
        'filename':file.name,
        'type':'png',
        'data':encode
    }
    g.create(**data)
 
    return {'name': file.name, 'len': file.size}




@router.get('/get-gallery-image-pickle/')
def get_gallery_image_pickle(request):
    file = open(filename,'rb')
    encoded_data =  file.read()
    file.close()
    decoded_data=base64.decodebytes((encoded_data))
    # decoded_data.decode('ascii')
    
    img_file = open(image_filename, 'wb')
    img_file.write(decoded_data)
    img_file.close()

            
    return {'id':23}



@router.get('/get-gallery-image/', response=List[GalleryOut])
def get_gallery_image(request):
    '''Get gallery image'''
    gallery = Gallery.objects.all()
    for x in gallery:
        formatted = eval(x.data)
        # print(type(formatted))
        decoded_data=base64.decodebytes(formatted)
  
        img_file = open(f"{image_filename}/{x.name}.png", 'wb')
        img_file.write(decoded_data)
        img_file.close()
    return gallery



@router.put('/update-gallery{id}/')
def update_image_gallery(request, id:int):
    '''
    Updating image api...
    '''
    return {"message":"Image API interface"}
