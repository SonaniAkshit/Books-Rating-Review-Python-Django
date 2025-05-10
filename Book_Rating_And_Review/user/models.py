from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(primary_key=True)
    contact = models.IntegerField(null=True, blank=True)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=100, null=True, blank=True, default=None)
    state = models.CharField(max_length=100, null=True, blank=True, default=None)
    pincode = models.IntegerField(null=True, blank=True, default=000)
    country = models.CharField(max_length=100, null=True, blank=True, default=None)
    profile_image = models.ImageField(upload_to='profile_pics/', null=True, blank=True, default='profile_pics/profile.png')

class Book(models.Model):
    book_name = models.CharField(max_length=100, null=True, blank=True)
    book_author = models.CharField(max_length=100, null=True, blank=True)
    book_price = models.CharField(max_length=100, null=True, blank=True)
    book_image =  models.ImageField(upload_to='book_pics/', null=True, blank=True)
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    book_name = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255, null=True, blank=True)
    user_profile = models.CharField(max_length=255, null=True, blank=True)
    review_title = models.CharField(max_length=255, null=True, blank=True)
    review_description = models.TextField(null=True, blank=True)
    rating = models.IntegerField(default=1)  # Ensure a default value
    date = models.DateTimeField(default=timezone.now)  # Correct use of timezone.now