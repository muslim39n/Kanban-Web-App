from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    telegram = models.SlugField(null=True)

