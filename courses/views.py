from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import FormView, CreateView, UpdateView, DeleteView

from courses.forms import CreateCourseForm, UpdateCourseForm
from courses.models import Course


def get_course(request):
    courses = Course.objects.all()

    return render(
        request=request,
        template_name='courses/list.html',
        context={
            'courses': courses,
        }
    )


class CreateCourseView(CreateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/create.html'


class UpdateCourseView(UpdateView):
    model = Course
    form_class = UpdateCourseForm
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/update.html'


class DeleteCourseView(DeleteView):
    pk_url_kwarg = 'pk'
    model = Course
    success_url = reverse_lazy('courses:list')
    template_name = 'courses/delete.html'

