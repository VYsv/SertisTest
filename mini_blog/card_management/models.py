from django.db import models

# Create your models here.
class Card(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    author = models.CharField(max_length=100)