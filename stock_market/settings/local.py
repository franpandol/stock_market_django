from .base import *

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
