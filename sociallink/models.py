from django.db import models

# Create your models here.
class SocialLink(models.Model):
    sl_name = models.CharField(max_length=255)
    sl_url = models.CharField(max_length=255)
    sl_icon = models.FileField(upload_to="social/",max_length=255,null=True,default=None)