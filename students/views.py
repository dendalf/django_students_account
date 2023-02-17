from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView

from webargs.djangoparser import use_args
from webargs.fields import Str

from core.views import CustomUpdateBaseView
from .forms import CreateStudentForm, UpdateStudentForm, StudentFilterForm
from .models import Student


def get_students(request):
    students = Student.objects.all().order_by('birthdate').select_related('group')

    filter_form = StudentFilterForm(data=request.GET, queryset=students)

    return render(
        request=request,
        template_name='students/list.html',
        context={
            'students': students,
            'filter_form': filter_form,
        }
    )


def detail_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/detail.html', {'title': f'Detail of {student.first_name} {student.last_name}','student': student})


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'title': 'Create Student',
            'form': form,
        }
    )


def update_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'GET':
        form = UpdateStudentForm(instance=student)
    elif request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            student.save()
            return HttpResponseRedirect(reverse('students:list'))

    return render(
        request=request,
        template_name='students/create.html',
        context={
            'title': 'Update Student',
            'form': form,
        }
    )


class UpdateStudent(CustomUpdateBaseView):  # custom view
    model = Student
    form_class = UpdateStudentForm
    success_url = 'students:list'
    template_name = 'students/create.html'


class UpdateStudentView(UpdateView):
    model = Student
    form_class = UpdateStudentForm
    success_url = reverse_lazy('students:list')
    template_name = 'students/create.html'


def delete_student(request, pk):
    st = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        st.delete()
        return HttpResponseRedirect(reverse('students:list'))
    else:
        return render(request, 'students/delete.html', {'student': st})

