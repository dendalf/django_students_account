# Generated by Django 4.1.5 on 2023-02-24 16:34

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_course_duration'),
        ('groups', '0004_group_course_alter_group_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='course', to='courses.course'),
        ),
        migrations.AlterField(
            model_name='group',
            name='end_date',
            field=models.DateField(default=datetime.datetime(2023, 5, 25, 16, 34, 53, 581891)),
        ),
    ]
