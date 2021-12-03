from django.db import models

from users.models import CustomUser 

class Organization(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(CustomUser)

    def __str__(self):
        return self.name