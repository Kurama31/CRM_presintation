from django.contrib import admin
from apps.scheduler.models import scheduler_days, task

admin.site.register(scheduler_days)
admin.site.register(task)
