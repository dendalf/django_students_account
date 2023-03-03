import datetime

from dateutil.relativedelta import relativedelta
from django.db import models
from faker import Faker

from core.validators import ValidateEmailDomain


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class PersonModel(BaseModel):
    valid_domains = ('gmail.com', 'yahoo.com', 'test.com')
    first_name = models.CharField(max_length=50, verbose_name='First name', db_column='f_name',)
    last_name = models.CharField(max_length=50, verbose_name='Last name', db_column='l_name')
    birthdate = models.DateField(default=datetime.date.today)
    city = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(validators=[ValidateEmailDomain(*valid_domains)])
    phone_number = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def get_age(self):
        return relativedelta(datetime.date.today(), self.birthdate).years

    @classmethod
    def _generate(cls):
        f = Faker()

        first_name = f.first_name()
        last_name = f.last_name()
        obj = cls(
            first_name=first_name,
            last_name=last_name,
            birthdate=f.date_between(start_date='-25y', end_date='-18y'),
            email=f'{first_name.lower()}.{last_name.lower()}@{f.random.choice(cls.valid_domains)}',
            city=f.city()
        )
        # obj.save()

        return obj

    @classmethod
    def generator(cls, cnt):
        for _ in range(cnt):
            cls._generate()

