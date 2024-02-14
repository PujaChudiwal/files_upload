# Create your models here.
from django.core.files.base import ContentFile
from django.db import models
import csv
from io import StringIO

class Blog(models.Model):
    name = models.CharField(
        max_length=250,
        verbose_name='NAME',
        null=True,
        default=None
    )
    file_upload = models.FileField(
        upload_to='input/',
        max_length=250,
        null=True,
        default=""
    )


    def save(self, *args, **kwargs):
        if self.file_upload:
            text_content = self.file_upload.read().decode('ascii').splitlines()
            csv_content = StringIO()
            csv_writer = csv.writer(csv_content)

            csv_writer.writerow(csv.reader(text_content))
            self.file_upload.save(
                self.file_upload.name.replace('.txt', '.csv'),
                ContentFile(csv_content.getvalue()),
                save=False           # # Avoid recursive save

            )




    def __str__(self):
        return self.name