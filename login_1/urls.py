from django.contrib import admin
from django.urls import path,include
from login_1.views import register_1,login_1,logout_1
from . import views

urlpatterns = [
    path('register',views.register_1,name='register'),
    path('login',views.login_1,name='login'),
    path('logout',views.logout_1,name='logout'),

]
