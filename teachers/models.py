import datetime
from dateutil.relativedelta import relativedelta

from django.db import models


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last_name')
    birthdate = models.DateField(default=datetime.date.today)
    salary = models.IntegerField()

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
