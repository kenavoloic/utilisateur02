from django.contrib import admin
from configurations.models import  Conducteur, Service, Site, GroupePage, Page

admin.site.register(Conducteur)
admin.site.register(Service)
admin.site.register(Site)
admin.site.register(GroupePage)
admin.site.register(Page)
# Register your models here.
