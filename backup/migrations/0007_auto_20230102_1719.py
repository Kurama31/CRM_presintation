# Generated by Django 3.2.13 on 2023-01-02 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0006_remove_task_manager_work_days_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task_manager_work_days',
            name='profile_id',
        ),
        migrations.AddField(
            model_name='task_manager_work_days',
            name='user_id',
            field=models.IntegerField(default=1, verbose_name='user_id'),
            preserve_default=False,
        ),
    ]
