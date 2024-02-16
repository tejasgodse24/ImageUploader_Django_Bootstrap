from django.http import HttpResponseRedirect
from django.shortcuts import render
from myapp.forms import ImageForm
from myapp.models import *

# Create your views here.

def index(request):

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path_info)

    context = {
        'form' : ImageForm(),
        'images' : Image.objects.all()
    }
    return render(request, 'myapp/index.html', context)