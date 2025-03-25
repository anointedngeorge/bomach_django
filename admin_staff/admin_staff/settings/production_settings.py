
from decouple import config
from pathlib import Path
import os
from admin_staff.jazzime import *
from admin_staff.jazzime_ui import *  
from admin_staff.ckeditor import *
from admin_staff.cronJob import *
from admin_staff.celery_config import *
import dj_database_url
import sys
from .core_apps import CORE_APPS



APPS_DIR = os.path.abspath('../myapps')
sys.path.append(APPS_DIR)



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = 'django-insecure-=af--evn#t-51+v#xb9@iefqh8kze0@ihe$_(%z0otqb@v#p!$'

DEBUG = True

SITE_ID = 1

ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['https://dash.bgbot.app']

ADMIN_LOGIN_PATH = 'admin/'
ADMIN_URI = "/admin"
# Application definition

INSTALLED_APPS = [
    # 'dashboard.apps.DashboardConfig',
    'django.contrib.admin',
    'authuser',
    'django.contrib.auth',
    'django.contrib.sites',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    #  "debug_toolbar",
]

INSTALLED_APPS += CORE_APPS

# specify the new user model for this app
AUTH_USER_MODEL = 'authuser.User'

CKEDITOR_UPLOAD_PATH="uploads/"


INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'authuser.middleware.SetLoggedinUserRoleAsGroup',
    "django_htmx.middleware.HtmxMiddleware",
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'admin_staff.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],

        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'admin_staff.custom_context_processors.get_system_settings_json',
                'admin_staff.context_processor.contextProcessor',
            ],
        },
    },
]



WSGI_APPLICATION = 'admin_staff.wsgi.application'
ASGI_APPLICATION = 'admin_staff.asgi.application'


# CHANNEL_LAYERS = {
#     'default': {
#         'BACKEND': 'channels_redis.core.RedisChannelLayer',
#         'CONFIG': {
#             "hosts": [('redis', 6379)],
#         },
#     },
# }

# database connection

DATABASES = {
        'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('DATABASE_NAME'),
        'USER': config('DATABASE_USER'),
        'PASSWORD': config('DATABASE_PASS'),
        'HOST': 'localhost',
        'PORT': '3306',
    }
}




CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# if config('ENVIRONMENT') == 'production':
#     AWS_ACCESS_KEY_ID = config('BUCKETEER_AWS_ACCESS_KEY_ID')
#     AWS_SECRET_ACCESS_KEY = config('BUCKETEER_AWS_SECRET_ACCESS_KEY')
#     AWS_STORAGE_BUCKET_NAME = config('BUCKETEER_BUCKET_NAME')
#     AWS_S3_REGION_NAME = config('BUCKETEER_AWS_REGION')
#     DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


MEDIA_ROOT = os.path.abspath('../media')
STATIC_ROOT = os.path.abspath('../static')
MEDIA_ROOT_MAIN = MEDIA_ROOT if os.path.exists(MEDIA_ROOT) else 'media/'
STATIC_ROOT_MAIN = STATIC_ROOT if os.path.exists(STATIC_ROOT) else 'static/'

sys.path.append(MEDIA_ROOT_MAIN)
sys.path.append(STATIC_ROOT_MAIN)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "/static/"
MEDIA_URL = "/media/"

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# CELERY_TIMEZONE = "Australia/Tasmania"
# CELERY_TASK_TRACK_STARTED = True
# CELERY_TASK_TIME_LIMIT = 30 * 60


# email settings
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = "mail.bomachgroup.com"
EMAIL_PORT = 26
EMAIL_HOST_USER = "support@bomachgroup.com"
EMAIL_HOST_PASSWORD = "Gfh2C?*oWI@^"
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False




# CELERY_BROKER_URL = "redis://redis:6379"
# CELERY_RESULT_BACKEND = "redis://redis:6379"

# CELERY_BEAT_SCHEDULE = {
#     "sample_task": {
#         "task": "core.tasks.sample_task",
#         "schedule": crontab(minute="*/1"),
#     },
# }
