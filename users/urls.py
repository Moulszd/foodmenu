from . import views
from django.urls import path
from django.contrib.auth import views as authentication_views


app_name = 'users' # it help django to differentialte urls between apps

urlpatterns = [
    path('register/', views.Register.as_view(), name='index'),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LoginView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', views.profilepage, name='profile'),
]
