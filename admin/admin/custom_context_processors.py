import datetime
import os

def get_system_settings_json(request):
    # /home/eit/DjangoProjects/bomach_django/system.json
    filepath =  os.path.abspath("/admin/system.json")
    if os.path.exists(filepath):
        readfile =  open(filepath, 'r').read()
        evaluated =   eval(readfile)
        return {
            'setting_items':evaluated.items()
        }
    else:
        print('No')
        return {}
