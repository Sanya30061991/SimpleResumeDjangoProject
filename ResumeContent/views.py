from django.shortcuts import render

# Create your views here.

def contacts(request):
    return render(request, 'ResumeContent/contacts.html')

def skill(request):
    return render(request, 'ResumeContent/skills.html')

def webPages(request):
    return render(request, 'ResumeContent/sites-info.html')

def start(request):
    return render(request, 'ResumeContent/starting.html')