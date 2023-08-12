from django.db import models

# Create your models here.
class Projects(models.Model):
    p_id = models.AutoField(auto_created = True, primary_key = True, serialize = False, verbose_name ='P_ID')
    p_title = models.CharField(max_length=255)
    p_short = models.CharField(max_length=255)
    p_description = models.TextField()
    p_img = models.FileField(upload_to='projects/', max_length=255, null=True, default=None)