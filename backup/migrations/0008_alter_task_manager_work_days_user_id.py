# Generated by Django 3.2.13 on 2023-01-21 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0007_auto_20230102_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task_manager_work_days',
            name='user_id',
            field=models.IntegerField(unique_for_date='date_begin', verbose_name='user_id'),
        ),
    ]
