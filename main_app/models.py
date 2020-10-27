from django.db import models
from django import forms


# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    even = models.IntegerField(default=1, name='Input an even number', blank=False )
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.first_name
