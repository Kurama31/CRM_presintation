# Generated by Django 3.2.13 on 2022-12-11 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0002_alter_task_manager_work_days_profile_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task_manager_work_days',
            old_name='date_begin',
            new_name='date',
        ),
        migrations.RemoveField(
            model_name='task_manager_work_days',
            name='date_end',
        ),
    ]