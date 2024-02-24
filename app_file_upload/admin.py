from django.contrib import admin
from django.http import HttpResponse
from .models import File


# Register your models here.

class YourModelAdmin(admin.ModelAdmin):
    list_display = ("name", "file_upload") # Add any other fields you want to display






admin.site.register(File, YourModelAdmin)
