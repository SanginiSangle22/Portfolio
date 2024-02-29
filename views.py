from django.shortcuts import render, redirect
from django.http import HttpResponse

import os

from .models import Profile, Resume, Skills, SkillService, Contact, Service, Portfolio, Portfolio_description, Maps
# Create your views here.
def home(request):
    profile = Profile.objects.all()
    context = {
        'profile': profile[0]
    }
    return render(request, 'main/index.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        contact = Contact(name=name, phone=phone, email=email, message=message)
        contact.save()
        return redirect('home')
      
    maps = Maps.objects.all()
    profile = Profile.objects.all()
    context = {
        'maps': maps[0],
        'profile': profile[0]
    }
    return render(request, 'main/contact.html', context)

def service(request):
    services = Service.objects.all()
    skills = Skills.objects.all()
    descriptions = SkillService.objects.all()
    context = {
        'skills':skills,
        'descriptions':descriptions[0],
        'services': services,
    }
    return render(request, 'main/service.html', context)



def portfolio(request):
    projects = Portfolio.objects.all()
    desc = Portfolio_description.objects.all()
    context = {
        'projects':projects,
        'desc': desc[0]
    }
    return render(request, 'main/portfolio.html', context)


def download_resume(request): 
    resume = Resume.objects.get(pk=1).resume
    path = resume.path
    
    with open(path, 'rb') as f:
        response = HttpResponse(f.read(), content_type = 'application/pdf')
        response['Content-Length'] = os.path.getsize( path )
        response['Content-Disposition'] = 'attachment; filename=%s/' % "SanginiSangle_Resume" + '.PDF'
        return response
    
    