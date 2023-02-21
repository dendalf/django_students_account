from django import forms
from django.core.exceptions import ValidationError

from students.models import Student
from .models import Group


class BaseGroupForm(forms.ModelForm):
    students = forms.ModelMultipleChoiceField(queryset=None, required=False)
    #
    # def save(self, commit=True):
    #     new_group = super().save(commit)
    #     students = self.cleaned_data['students']
    #     for student in students:
    #         student.group = new_group
    #         student.save()

    class Meta:
        model = Group
        fields = '__all__'

        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'})
        }


class CreateGroupForm(BaseGroupForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.filter(group_id__isnull=True)

    class Meta(BaseGroupForm.Meta):
        exclude = [
            'headman',
        ]


class UpdateGroupForm(BaseGroupForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['students'].queryset = Student.objects.all().select_related('group')
        self.fields['headman_field'] = forms.ChoiceField(
            choices=[(st.pk, f'{st.first_name} {st.last_name}') for st in self.instance.students.all()],
            label='Headman',
            required=False
        )
        self.fields['headman_field'].choices.insert(0, (0, '---------'))

    class Meta(BaseGroupForm.Meta):
        exclude = [
            'headman'
        ]

