# Generated by Django 3.2.13 on 2023-01-02 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0004_auto_20221212_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='task_manager_work_days',
            name='user_id',
            field=models.IntegerField(default=1, verbose_name='get_user_id'),
            preserve_default=False,
        ),
    ]
