# Generated by Django 3.2.13 on 2023-11-05 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0006_auto_20231104_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2023-11-05'),
        ),
    ]
