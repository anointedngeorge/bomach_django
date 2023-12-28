import importlib
from authuser.models import *
from django.apps import apps

REGISTERED_APP = [
    # {'app':AgentNotification, 'list_display':['pk'], 'list_display_links':['pk'], 'exclude':[], "has_action":True},
]

mods =  apps.get_models()
for m in mods:
    app_name = m.__name__
    module = f"{m._meta.model.__module__}.{app_name}"
    REGISTERED_APP.append(module)
   
# {
#     'app':module, 
#     'list_display':['pk'], 
#     'list_display_links':['pk'], 
#     'exclude':[], 
#     "has_action":False,
#     "is_registered":True
# }

# def list_display():
#     return ['pk']
# def list_display_links():
#     return ['pk']
# def exclude():
#     return []
# def has_action():
#     return False
# def is_registered():
#     return True