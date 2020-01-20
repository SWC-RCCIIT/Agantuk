from django.db import models

# Create your models here.
class User_Login(models.Model):
    Name = models.CharField(max_length=50)