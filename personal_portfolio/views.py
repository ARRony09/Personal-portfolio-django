from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Project
from blog.models import Post

# Create your views here.

def home(request):
    project=Project.objects.all()
    
    return render(request,'portfolio/home.html',{'projects':project})
