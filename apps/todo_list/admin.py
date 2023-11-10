from django.contrib import admin

from apps.todo_list.models import Category, TodoList

admin.site.register(Category)
admin.site.register(TodoList)




