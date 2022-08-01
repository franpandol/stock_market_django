import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin


class LowerEmailField(models.EmailField):
    def get_prep_value(self, value):
        value = super(LowerEmailField, self).get_prep_value(value)
        if value is not None:
            value = value.lower()
        return value


class Account(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = LowerEmailField("Email", unique=True)
    name = models.CharField("Name", max_length=255)
    last_name = models.CharField("Last name", max_length=255)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", "last_name"]

    class Meta:
        verbose_name = "user"
        verbose_name_plural = "users"
