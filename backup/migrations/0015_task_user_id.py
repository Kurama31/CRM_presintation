# Generated by Django 3.2.13 on 2023-02-09 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler', '0014_alter_task_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='user_id',
            field=models.IntegerField(default=1, verbose_name='user_id'),
            preserve_default=False,
        ),
    ]
