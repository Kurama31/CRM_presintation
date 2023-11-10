#from django.contrib.auth import views
from django.urls import path
#from . import views
from apps.adminka import views as views

urlpatterns = [
    path('', views.adminka, name='adminka'),
    ]