from django.db import models

# Create your models here.
class Enquiry(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.TextField(max_length=500)