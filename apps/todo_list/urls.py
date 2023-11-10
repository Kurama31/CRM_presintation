from django.urls import path
from apps.todo_list import views as todo

urlpatterns = [
    path('', todo.todo_list, name='todo_list'),
]