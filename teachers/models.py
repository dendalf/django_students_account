import datetime
from dateutil.relativedelta import relativedelta

from django.db import models
from faker import Faker


class Teacher(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='first_name')
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='last_name')
    birthdate = models.DateField(default=datetime.date.today)
    salary = models.IntegerField()

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthdate).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            t = cls()
            t.first_name = f.first_name()
            t.last_name = f.last_name()
            t.birthdate = f.date_between(start_date='-65y', end_date='-21y')
            t.salary = f.pyint(min_value=300, max_value=10000, step=100)
            t.save()
