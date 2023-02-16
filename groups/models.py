import datetime
from dateutil.relativedelta import relativedelta

from django.db import models
from faker import Faker

from core.models import BaseModel
from core.validators import validate_start_date
from teachers.models import Teacher


class Group(BaseModel):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        db_column='group_name'
    )
    start_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    end_date = models.DateField(default=datetime.datetime.now() + datetime.timedelta(days=90))
    group_description = models.TextField(
        max_length=50,
        verbose_name='Group description',
        db_column='group_description',
        null=True,
        blank=True
    )
    headman = models.OneToOneField('students.Student', on_delete=models.SET_NULL, null=True, blank=True, related_name='headman_group')
    teachers = models.ManyToManyField(to=Teacher, blank=True, related_name='group_teachers')
    course = models.OneToOneField('courses.Course', on_delete=models.SET_NULL, null=True, related_name='course')

    class Meta:
        db_table = 'groups'

    def __str__(self):
        return f'{self.group_name}'

    @classmethod
    def generate_fake_data(cls, cnt):
        f = Faker()
        group_names = ['Python', 'JavaScript', 'C++', 'C#', 'Project Manager', 'DevOps', 'QA']
        for _ in range(cnt):
            s = cls()
            s.group_name = f.random.choice(group_names)
            s.save()
