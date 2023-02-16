from django.db import models

from core.models import BaseModel


class Course(BaseModel):
    course_name = models.CharField(max_length=50, verbose_name='Course name', db_column='c_name')
    course_duration = models.IntegerField(verbose_name='Course duration(weeks)')

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return f'{self.course_name}'

