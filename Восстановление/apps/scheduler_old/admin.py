from django.contrib import admin
from apps.scheduler_old.models import Scheduler_DB, company_staff, Origin

admin.site.register(Scheduler_DB)
admin.site.register(company_staff)
admin.site.register(Origin)
