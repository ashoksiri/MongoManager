from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    pass

class Database(models.Model):
    db_type = models.CharField(max_length=20)
    host = models.CharField(max_length=100, unique=True)
    port = models.IntegerField()
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    options = models.TextField()

    def __str__(self):
        return "{}@{}".format(self.db_type,self.host)