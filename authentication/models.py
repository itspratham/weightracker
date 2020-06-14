from django.db import models

# Create your models here.


class User(models.Model):
    email       = models.EmailField(blank=False,null=False)
    password    = models.CharField(max_length=20,blank=False,null=False)

    def __str__(self):
        return str(self.email)

class UserProfile(models.Model):
    email        = models.EmailField(max_length=50, blank=False, null=False,unique=True)
    password     = models.CharField(max_length=20,null=False,blank=False)
    first_Name   = models.CharField(max_length=500, blank=False,null=False)
    last_Name    = models.CharField(max_length=500,blank=False, null=False)
    Dob          = models.DateField(null=False, blank=False)
    authorized   = models.CharField(default='N', max_length=20)
    user_since   = models.DateTimeField(auto_now_add=True)
    status       = models.CharField(default='Y', max_length=500)
    weight       = models.FloatField(max_length=10)
    photo        = models.ImageField(upload_to="authentication/media/%Y/%m/%d/")

    def __str__(self):
        return str(self.first_Name + " " + self.last_Name)