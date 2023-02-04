import datetime
from dateutil.relativedelta import relativedelta

from django.db import models

from core.validators import validate_start_date


class Group(models.Model):
    group_name = models.CharField(
        max_length=50,
        verbose_name='Group name',
        db_column='group_name'
    )
    start_date = models.DateField(default=datetime.date.today, validators=[validate_start_date])
    end_date = models.DateField(default=datetime.date.today)
    group_description = models.TextField(
        max_length=50,
        verbose_name='Group description',
        db_column='group_description'
    )

    class Meta:
        db_table = 'groups'

