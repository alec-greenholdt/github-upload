
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView 
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

def polls(request):
    return HttpResponse("Polls Tab")

class HomeView(TemplateView):
    template_name= 'templates/mainsite/home.html'

# fucntion of class above
# def home(request):
#     return render(request,'templates/mainsite/home.html',)


class AuthorizedView(LoginRequiredMixin ,TemplateView):
    loginUrl='/admin'
    template_name= 'templates/registration/authorized.html'
    
#function of class above
# @login_required(login_url='/admin')
# def authorized(request):
#     return render(request, 'templates/registration/authorized.html',{})

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url= reverse_lazy("login")
    template_name = "registration/signup.html"
