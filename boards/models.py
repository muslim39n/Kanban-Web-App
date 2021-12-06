from django.db import models
from organizations.models import Organization
from users.models import CustomUser


class Board(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    admins = models.ManyToManyField(CustomUser, related_name='admins')
