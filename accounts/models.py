from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts')
    
    def __str__(self):
        return str(self.user)


PHONE_CHOICES = (
    ('Perimary' , 'Perimary' ),
    ('Secondery' , 'Secondery'),
    )



class Phones(models.Model):
    user = models.ForeignKey(User,related_name='user_phone',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=PHONE_CHOICES)
    phone = models.CharField(max_length=20)
    

    def __str__(self):
        return str(self.user)


ADDRESS_CHOICES = (
    ('Home' , 'Perimary' ),
    ('Office' , 'Office'),
    ('Bussines' , 'Bussines'),
    ('Academy' , 'Academy'),
    ('Other' , 'Other'),
    )


class Address(models.Model):
    user = models.ForeignKey(User,related_name='user_address',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=ADDRESS_CHOICES)
    address = models.TextField(max_length=200)
    

    def __str__(self):
        return str(self.user)