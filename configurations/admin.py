from django.contrib import admin
from configurations.models import  Conducteur, Service, Site, GroupePage, Page, AssociationUtilisateurGroupe, PageConfig

admin.site.register(Conducteur)
admin.site.register(Service)
admin.site.register(Site)
admin.site.register(GroupePage)
admin.site.register(Page)
admin.site.register(AssociationUtilisateurGroupe)
admin.site.register(PageConfig)
# Register your models here.
