from django.shortcuts import render

# Create your views here.

def webPages(request):
    return render(request, 'ResumeContent/sites-info.html')

def start(request):
    return render(request, 'ResumeContent/starting.html')