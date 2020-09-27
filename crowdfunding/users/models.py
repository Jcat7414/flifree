from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    # password = models.CharField(max_length=80, verbose_name="password")
    first_name = models.CharField(max_length=50, verbose_name="first name")
    last_name = models.CharField(max_length=50, verbose_name="last name")
    image = models.URLField(max_length=200, verbose_name="profile photo", default="https://via.placeholder.com/300.jpg")
    bio = models.TextField(max_length=1000, verbose_name="biography")
    phone = models.CharField(max_length=13, verbose_name="phone number")
    location = models.CharField(max_length=100, verbose_name="location")
    newsletter_signup = models.BooleanField(verbose_name="subscribe to newsletter")
    terms_privacy = models.BooleanField(verbose_name="accept Terms & Privacy")
    founder = models.BooleanField(verbose_name="founder")
    supporter = models.BooleanField(verbose_name="supporter")
    is_staff = models.BooleanField(verbose_name="admin")
    created_on = models.DateTimeField(verbose_name="created on")
   
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    def __str__(self):
        return self.username
