from .base import *

import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env.dev")
load_dotenv(dotenv_path, verbose=True)

SECRET_KEY = os.getenv("SECRET_KEY", "xjase%kwv6=d6!r$#a)yv%$$m1x)fp-53jc&s)4=i1w$9l")

DEBUG = True
ALLOWED_HOSTS = ["*"]

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", "demo")
