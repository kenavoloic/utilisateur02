from django.contrib import admin
from django.urls import include, path
#from .views import CustomAdminLoginView

urlpatterns = [
    #path('admin/login/', CustomAdminLoginView.as_view(), name='admin_login'),
    path('admin/', admin.site.urls),
    path('', include('configurations.urls')),
]
