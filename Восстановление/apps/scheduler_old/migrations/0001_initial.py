# Generated by Django 3.2.10 on 2022-04-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='scheduler_old',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(verbose_name='is active')),
                ('date', models.DateTimeField(verbose_name='date of appointment')),
                ('comment', models.CharField(max_length=300, verbose_name='comment')),
                ('client_name', models.CharField(max_length=100, verbose_name='comment')),
                ('client_lastname', models.CharField(max_length=100, verbose_name='comment')),
                ('doctor_name', models.CharField(max_length=100, verbose_name='comment')),
                ('Doctor_lastname', models.CharField(max_length=100, verbose_name='comment')),
                ('cabinet_number', models.CharField(max_length=3, verbose_name='comment')),
            ],
            options={
                'verbose_name': 'Запись',
                'verbose_name_plural': 'Запись_расписание',
            },
        ),
    ]
