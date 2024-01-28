# Create your models here.
from django.db import models

class Blog(models.Model):
    file_upload = models.FileField(upload_to='uploads/', max_length=250, null=True, default=None)