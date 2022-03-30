from django.urls import path

from . import views

urlpatterns= [
    path('home',views.HomeView.as_view(), name='home'),
    path("signup", views.SignUp.as_view(), name="signup"),
    path('authorized', views.AuthorizedView.as_view()),
]