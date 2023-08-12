from django.db import models

# Create your models here.
class WebService(models.Model):
    service_id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='S_ID')
    service_img = models.FileField(upload_to="webservices/",max_length=255,null=True,default=None)
    service_title = models.CharField(max_length=100)
    service_sub = models.CharField(max_length=255)