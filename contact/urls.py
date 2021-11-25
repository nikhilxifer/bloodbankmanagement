from bloodbankmanagement.routers.db_rrouter import search
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView,LoginView

from blood import views
from contact import views

urlpatterns = [
     path('contact',views.contact,name='c11'),
]
