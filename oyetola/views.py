from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, Template
from .models import Blog

# Create your views here.

def index(request):
    blogs = Blog.objects.all()
    return render(request, 'oyetola/site.html', {'blogs':blogs})
    # return HttpResponse('<p>fjfjfjfj</p>')
