from django.db import models
from django.contrib.auth.models import AbstractUser


        

class Employee(AbstractUser):
    username = models.CharField(max_length=155, unique=True)
    

    USERNAME_FIELD = 'username'
    
    def __str__(self):
        return self.username