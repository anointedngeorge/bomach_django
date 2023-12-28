from reports.models import *


def updateEngineeringReport(model:object, request:object, data:dict, filter_data:dict):
    try:
        md =  model.objects.all()
        if md.filter(id=filter_data.get('id')).exists():
            md.filter(id=filter_data.get('id')).update(**data)
            message = True
        else: message = False
        return message
    except Exception as e:
        print(e)
        return False


def contactSenderEngineeringReport(model:object, request:object, data:dict, filter_data:dict):
    try:
        md =  model.objects.all()
        if md.filter(id=filter_data.get('id')).exists():
            details = md.filter(id=filter_data.get('id')).get()
            print(details)
            message = True
        else: message = False
        return message
    except Exception as e:
        print(e)
        return False