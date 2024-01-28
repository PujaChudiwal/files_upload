from django.urls import path
from . import views

urlpatterns = [
    path('UploadFile', views.UploadFile, name='UploadFile'),
]