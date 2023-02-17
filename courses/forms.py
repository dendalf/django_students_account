from django import forms

from courses.models import Course


class BaseCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

        widgets = {
            'course_duration': forms.NumberInput()
        }


class CreateCourseForm(BaseCourseForm):

    class Meta(BaseCourseForm.Meta):
        pass


class UpdateCourseForm(BaseCourseForm):

    class Meta(BaseCourseForm.Meta):
        pass

