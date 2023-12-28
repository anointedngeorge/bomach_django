from decouple import config
import os



if config("ENVIRONMENT") == "production":
    from admin.settings.production_settings import *
else:
    from admin.settings.development_settings import *
