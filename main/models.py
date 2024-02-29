from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=13, null=True, blank=True)
    address = models.CharField(max_length=1000, null = True, blank=True)
    # profile_img = models.ImageField(blank=True, upload_to='images', default='images/profile.jpg')
    profile_img = models.CharField(max_length=1000)
    about_me = models.TextField(max_length=5000, blank=True, null=True)
    tagline = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return str(self.user.username) + " (Edit this)"
        

class Resume(models.Model):
    resume = models.FileField(upload_to='resume')  
    def __str__(self):
        return "Edit Resume here" 
    
            
class Skills(models.Model):
    skill = models.CharField(max_length=100, null=True, blank=True)
    level = models.IntegerField(null=True, blank=True)
    
    def __str__(self):
        return self.skill
    
class SkillService(models.Model):
    about_skill = models.CharField(max_length=1000, null=True, blank=True)
    about_service = models.CharField(max_length=1000, null=True, blank=True)
    
    def __str__(self):
        return "Write about your skills and Services (Edit this)"    


class Service(models.Model):
    service =  models.CharField(max_length=100, null=True, blank=True)
    service_css_class = models.CharField(max_length=100, null=True, blank=True, verbose_name='visit https://themify.me/themify-icons')
    
    def __str__(self):
        return self.service
    
    

class Contact(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    email = models.EmailField(blank=True, null=True)
    message  = models.TextField(max_length=2000, null=True)
    
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.name) + " ------------------------------------------------> " + str(self.date)
    

class Portfolio(models.Model):
    project_title = models.CharField(max_length=100, null=True, blank=True)
    project_link = models.CharField(max_length=1000 , null=True, blank=True)
    # img = models.ImageField(upload_to='images', default='images/project.png', null=True, verbose_name='img: (1920 x 1080)')
    img = models.CharField(max_length=1000, null=True, verbose_name='img: (1920 x 1080)')
    
    def __str__(self):
        return self.project_title
    
    
 
class Portfolio_description(models.Model):
    desc  = models.TextField(max_length=5000, null=True)
    
    def __str__(self):
        return "Add description for portfolio (Edit this)"    
    
    
class Maps(models.Model):
    map = models.CharField(max_length=100, null=True, verbose_name='Enter address, to confirm if it is avaible visit: https://embed-googlemap.com/') 
    
    def __str__(self):
        return "Add adress for map (Edit this)"
    
       