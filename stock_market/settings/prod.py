from .base import *

from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env.prod')
load_dotenv(dotenv_path, verbose=True)

SECRET_KEY = os.getenv("SECRET_KEY")

DEBUG = False
ALLOWED_HOSTS = ['challenges.pandol.sh', ]
DATABASES = {
    'default': {
        'NAME': os.getenv("DATABASE_NAME"),
        'USER': os.getenv("DATABASE_USER"),
        'PORT': os.getenv("DATABASE_PORT"),
        'PASSWORD': os.getenv("DATABASE_PASSWORD"),
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': os.getenv("DATABASE_HOST"),
    }
}

