from django.db import models

# Create your models here.
class Image:
    imageid:int
    imagename:str
    from django.db import models

class Image(models.Model):  # Use models.Model to define a Django model
    imagename = models.ImageField(upload_to='images/')  # Use ImageField to store image files

# class online:
#     id:int
#     first_name:str
#     last_name:str
#     email:str
    
# models.py

from django.db import models

# class OnlineUser(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     email = models.EmailField()
#     password = models.CharField(max_length=255)
#     confirm_password = models.CharField(max_length=255)
 
class Online(models.Model):
    id:int
    first_name:str
    last_name:str
    email:str
    password:str