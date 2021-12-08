from django.db import models
from organizations.models import Organization
from users.models import CustomUser


class Board(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    creator = models.ForeignKey(CustomUser, null=True, on_delete=models.SET_NULL)
    admins = models.ManyToManyField(CustomUser, related_name='admins', blank=True)

    def __str__(self):
        return self.title + ' > ' + self.organization.name


class Stage(models.Model):
    name = models.CharField(max_length=32)
    number = models.PositiveSmallIntegerField()
    board = models.ForeignKey(Board, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ' > ' + self.board.title
    
