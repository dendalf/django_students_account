from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible
# from .models import Student

DOMAINS = ('gmail.com', 'yahoo.com')


def validate_email_domain(value):
    # domains = ('gmail.com', 'yahoo.com', 'test.com')
    domain = value.split('@')[-1]
    if domain not in DOMAINS:
        raise ValidationError('Your domain is not correct!')

#
# def validate_unique_email(value):
#     students = Student.objects.all()
#     for st in students:
#         if value.lower() == st.email.lower():
#             raise ValidationError('Your email is not unique!')


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

