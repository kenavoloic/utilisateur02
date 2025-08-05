from django.contrib import admin
from configurations.models import  Conducteur, Service, Site

admin.site.register(Conducteur)
admin.site.register(Service)
admin.site.register(Site)
# Register your models here.
