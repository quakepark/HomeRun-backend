from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Registration(models.Model):

    First_Name = models.CharField(max_length=100)
    Last_Name = models.CharField(max_length=100)
    Address = models.CharField(max_length=200)
    Email_Address = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=timezone.now)
    Phone_Number = models.IntegerField()
