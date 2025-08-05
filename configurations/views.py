from django.shortcuts import render
from django.http import HttpResponse
# crispy-form
from django.contrib.auth.views import LoginView
#from .forms import CustomLoginForm
# redirection en cas d'erreur de connexion sur la page admin
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.urls import reverse_lazy

# class CustomLoginView(LoginView):
#     form_class = CustomLoginForm
#     template_name = 'pages/connexion.html'
    
def accueil(request):
    return HttpResponse('accueil')

def pageA(request):
    return HttpResponse('pageA')

def pageB(request):
    return HttpResponse('pageB')

def pageC(request):
    return HttpResponse('pageC')


# class CustomAdminLoginView(LoginView):
#     template_name = 'admin/login.html'
    
#     def form_invalid(self, form):
#         # Redirection vers l'accueil en cas d'erreur
#         return redirect('/') 
