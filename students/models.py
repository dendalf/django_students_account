
from random import choice
from django.db import models
from django.db.models.signals import pre_init, post_init, pre_save, post_save
from django.dispatch import receiver

from core.models import PersonModel
from groups.models import Group

VALID_DOMAINS = ('gmail.com', 'yahoo.com', 'test.com')


class Student(PersonModel):
    group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, related_name='students')

    class Meta:
        db_table = 'students'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    @classmethod
    def _generate(cls):
        groups = Group.objects.all()
        student = super()._generate()
        student.group = choice(groups)
        student.save()


@receiver(pre_init, sender=Student)
def pre_init_signal(sender, **kwargs):
    print(f'Pre INIT: {kwargs}')


@receiver(post_init, sender=Student)
def post_init_signal(sender, **kwargs):
    print(f'Post INIT: {kwargs}')


@receiver(pre_save, sender=Student)
def pre_save_signal(sender, **kwargs):
    print(f'Pre SAVE: {kwargs}')


@receiver(post_save, sender=Student)
def post_save_signal(sender, **kwargs):
    print(f'Post SAVE: {kwargs}')

