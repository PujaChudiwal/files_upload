from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from .forms import BlogForm

def UploadFile(request):
    if request.method == 'POST':
        form = BlogForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('The file is saved')
    else:
        form = BlogForm()
    context = {'form':form,}
    return render(request, 'upload.html', context)