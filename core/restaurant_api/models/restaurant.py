
from django.db import models


class Restaurant(models.Model):

    title = models.CharField(max_length=150, verbose_name="Restaurant name")

    
    class Meta:
        verbose_name = ("Restaurant")
        verbose_name_plural = ("Restaurants")
        
    
    def __str__(self) -> str:
        return self.title