from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FileForm
from django.http import HttpResponse
from .models import File

def UploadFile(request):
    if request.method == 'POST':
        form = FileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = FileForm()
        context = {'form': form}
        return render(request, 'upload.html', context)
    context = {'form': FileForm}