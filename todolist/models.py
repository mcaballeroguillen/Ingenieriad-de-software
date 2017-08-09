from __future__ import unicode_literals
from django.db import models



class Todo(models.Model):
    actividad=models.CharField(max_length=100)
    prioridad=models.IntegerField()
    def __str__(self):
        return self.actividad


