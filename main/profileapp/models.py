from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    name = models.CharField(default='name', max_length=200, null=True)
    genderChoice = (("M","Male"),("F","Female"),("o","Other"))
    gender = models.CharField(max_length = 1,choices=genderChoice,default='M')
    dob = models.DateTimeField(blank=True, null=True)
    age = models.IntegerField( blank=True, null=True)
    address_text = 'address'
    address = models.CharField(default = address_text, max_length=200, null=True)
   

    def __str__(self):
        return f"{self.user.username}'s profile"
