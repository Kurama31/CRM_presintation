# Generated by Django 3.2.13 on 2022-07-28 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduler_old', '0016_origin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduler_db',
            name='staff_lastname',
            field=models.CharField(max_length=100, unique_for_date='date_begin', verbose_name='staff_lastname'),
        ),
    ]
