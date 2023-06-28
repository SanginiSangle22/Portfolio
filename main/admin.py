from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Profile)
admin.site.register(models.Resume)
admin.site.register(models.Skills)
admin.site.register(models.SkillService)
admin.site.register(models.Service)
admin.site.register(models.Portfolio)
admin.site.register(models.Portfolio_description)
admin.site.register(models.Maps)

class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ('name','email','phone','message','date')
    

admin.site.register(models.Contact,ContactAdmin)    