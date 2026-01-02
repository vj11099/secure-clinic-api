from django.utils import timezone
from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    gender = models.CharField()
    date_of_birth = models.CharField()
    updated_at = models.TimeField(default=timezone.now)

    class Meta:
        db_table = 'auth_user'
