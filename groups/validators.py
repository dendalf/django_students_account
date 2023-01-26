from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


def validate_start_date(value):
    if value < datetime.now().date():
        raise ValidationError('Your start date is not correct')

