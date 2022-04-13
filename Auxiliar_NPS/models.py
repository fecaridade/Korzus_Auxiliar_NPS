
from tokenize import Triple
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class Partner(AbstractUser):
    username = None
    email = models.EmailField(('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    
    def __str__(self):
        return self.email



class Client(models.Model):
    name = models.CharField(max_length=40)
    phone_number = models.CharField(max_length=20)
    rating_nps = models.IntegerField(null=True,blank=True)
    partener = models.ForeignKey(Partner,null=True,blank=True,on_delete=models.RESTRICT)
    

    def __str__(self):
        return self.name
        
    





        
    
    
    



