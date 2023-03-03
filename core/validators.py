from datetime import datetime

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

DOMAINS = ('gmail.com', 'yahoo.com')


def validate_email_domain(value):
    # domains = ('gmail.com', 'yahoo.com', 'test.com')
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError('Your domain is not correct!')


# def validate_unique_email(value):
#     from students.models import Student
#     students = Student.objects.all()
#     for st in students:
#         if value.lower() == st.email.lower():
#             raise ValidationError('Your email is not unique!')


# def validate_start_date(value):
#     if value < datetime.now().date():
#         raise ValidationError('Your start date is not correct')


@deconstructible
class ValidateEmailDomain:
    def __init__(self, *domains):
        if domains:
            self.domains = tuple(domains)
        else:
            self.domains = DOMAINS

    def __call__(self, *args, **kwargs):
        domain = args[0].split('@')[-1]
        if domain not in self.domains:
            raise ValidationError('Your domain is incorrect!')

