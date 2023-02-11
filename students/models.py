import datetime

from dateutil.relativedelta import relativedelta
from django.core.validators import MinLengthValidator
from django.db import models
from faker import Faker

from core.validators import ValidateEmailDomain, validate_unique_email
from groups.models import Group

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name', validators=[MinLengthValidator(2)])
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    birthdate = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*VALID_DOMAINS), validate_unique_email])
    phone_number = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthdate).years

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        for _ in range(cnt):
            s = cls()
            s.first_name = f.first_name()
            s.last_name = f.last_name()
            s.email = f'{s.first_name.lower()}.{s.last_name.lower()}@{f.random.choice(VALID_DOMAINS)}'
            s.birthdate = f.date_between(start_date='-25y', end_date='-18y')
            s.group = f.random.choice(Group.objects.all())
            s.save()

