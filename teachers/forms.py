from django import forms
from django.core.exceptions import ValidationError

from .models import Teacher


class CreateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'salary',
        ]

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(),
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()


class UpdateTeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'salary',
        ]

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'}),
            'salary': forms.NumberInput(),
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

