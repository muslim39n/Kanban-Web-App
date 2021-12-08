from django.db import models

from users.models import CustomUser 

class Organization(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(CustomUser, through='Membership', blank=True)

    def __str__(self):
        return self.name

class Membership(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)