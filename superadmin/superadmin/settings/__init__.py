from decouple import config
import os



if config("ENVIRONMENT") == "production":
    from superadmin.settings.production_settings import *
else:
    from superadmin.settings.development_settings import *
