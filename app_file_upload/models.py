from django.db import models
import pandas as pd
from io import StringIO
import os
from django.core.files.base import ContentFile
import csv


class File(models.Model):
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


    def __str__(self):
        return self.name




    def save(self, *args, **kwargs):
        if self.file_upload:
            file_extension = os.path.splitext(self.file_upload.name)[1].lower()

            if file_extension == '.xlsx':
                # Read the uploaded Excel file
                excel_df = pd.read_excel(self.file_upload)

                # Convert Excel content to CSV format
                csv_content = StringIO()
                excel_df.to_csv(csv_content, index=False)

                # Save the CSV content to a new file
                self.file_upload.save(
                    self.file_upload.name.replace('.xlsx', '.csv'),
                    ContentFile(csv_content.getvalue()),
                    save=False  # Avoid recursive save
                )

            elif file_extension == '.txt':
                # Read the uploaded text file
                text_content = self.file_upload.read().decode('ascii').splitlines()

                # Convert text content to CSV format
                csv_content = StringIO()
                csv_writer = csv.writer(csv_content)
                csv_writer.writerows(csv.reader(text_content))

                # Save the CSV content to a new file
                self.file_upload.save(
                    self.file_upload.name.replace('.txt', '.csv'),
                     ContentFile(csv_content.getvalue()),
                    save=False  # Avoid recursive save
                )

        super().save(*args, **kwargs)





