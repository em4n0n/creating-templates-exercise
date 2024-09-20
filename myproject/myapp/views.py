from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def about(request):
    about_content = {'about' : "hello"}
    return render(request, "about.html", about_content)