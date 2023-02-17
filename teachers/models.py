import datetime
from random import randint

from dateutil.relativedelta import relativedelta

from django.db import models
from faker import Faker

from core.models import PersonModel


class Teacher(PersonModel):
    salary = models.IntegerField()

    class Meta:
        db_table = 'teachers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def _generate(cls):
        teacher = super()._generate()
        teacher.birthdate = Faker().date_between(start_date='-65y', end_date='-18y')
        teacher.salary = randint(3, 100) * 100
        teacher.save()

