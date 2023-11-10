from django.urls import path
from . import views

urlpatterns = [
    path('', views.scheduler_main, name='scheduler_main'),
    #path('make_work_schedule', views.make_work_schedule, name='make_work_schedule'),
    #path('test', views.test, name='test'),
    ]