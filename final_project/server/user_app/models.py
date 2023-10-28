from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(null=False, blank=False, max_length=20)
    password = models.CharField(null=False, blank=False, max_length=20)