from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "configurations"

urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('connexion/', auth_views.LoginView.as_view(
        template_name='pages/connexion.html'
    ), name='connexion'),    
    # Page de logout
    path('deconnexion/', auth_views.LogoutView.as_view(), name='deconnexion'),
    path('pageA/', views.pageA, name="pageA"),
    path('pageB/', views.pageB, name="pageB"),
    path('pageC/', views.pageC, name="pageC"),
]    
