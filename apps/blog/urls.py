from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from apps.blog import views as views

urlpatterns = [
    path('', views.blog, name='blog_index'),
]