from decouple import config
import os



if config("ENVIRONMENT") == "production":
    from admin_staff.settings.production_settings import *
else:
    from admin_staff.settings.development_settings import *
