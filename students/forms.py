from django import forms
from django.core.exceptions import ValidationError

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'email',
            'birthdate',
            'phone_number',
        ]

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_phone_number(self):
        valid_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        value = self.cleaned_data.get('phone_number')
        res = ''.join(filter(lambda x: x in valid_symbols, value))  # оставляем только цифры
        if len(res) == 10:  # если пользователь ввел номер без международного кода
            return f'+38 ({res[0:3]}) {res[3:6]}-{res[6:8]}-{res[8:10]}'
        elif len(res) == 12:  # если пользователь ввел номер с международным кодом
            return f'+{res[0:2]} ({res[2:5]}) {res[5:8]}-{res[8:10]}-{res[10:12]}'
        else:
            raise ValidationError('Your phone number is incorrect!')


class UpdateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'first_name',
            'last_name',
            'birthdate',
            'phone_number',
        ]

        widgets = {
            'birthdate': forms.DateInput(attrs={'type': 'date'})
        }

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')
        return value.capitalize()

    def clean_phone_number(self):
        valid_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        value = self.cleaned_data.get('phone_number')
        res = ''.join(filter(lambda x: x in valid_symbols, value))  # оставляем только цифры
        if len(res) == 10:  # если пользователь ввел номер без международного кода
            return f'+38 ({res[0:3]}) {res[3:6]}-{res[6:8]}-{res[8:10]}'
        elif len(res) == 12:  # если пользователь ввел номер с международным кодом
            return f'+{res[0:2]} ({res[2:5]}) {res[5:8]}-{res[8:10]}-{res[10:12]}'
        else:
            raise ValidationError('Your phone number is incorrect!')


