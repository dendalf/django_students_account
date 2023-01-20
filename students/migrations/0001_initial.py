# Generated by Django 4.1.5 on 2023-01-19 15:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(db_column='f_name', max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(db_column='l_name', max_length=50, verbose_name='Last name')),
                ('birthdate', models.DateField(default=datetime.date.today)),
                ('city', models.CharField(blank=True, max_length=50, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
