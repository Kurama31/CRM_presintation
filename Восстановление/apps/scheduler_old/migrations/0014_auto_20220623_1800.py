# Generated by Django 3.2.13 on 2022-06-23 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_old', '0013_alter_scheduler_db_staff_lastname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='city',
        ),
        migrations.RemoveField(
            model_name='person',
            name='country',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Country',
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
