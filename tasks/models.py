from django.db import models

from boards.models import Stage

class Task(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField(null=True, blank=True)
    stage = models.ForeignKey(Stage, on_delete=models.CASCADE)
     
