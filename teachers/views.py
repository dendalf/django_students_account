from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateTeacherForm, UpdateTeacherForm
from .models import Teacher


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',

)
def get_teachers(request, args):
    teachers = Teacher.objects.all()

    if len(args) and (args.get('first_name') or args.get('last_name')):
        teachers = teachers.filter(
            Q(first_name__istartswith=args.get('first_name', '')) | Q(last_name__istartswith=args.get('last_name', ''))
        )

    return render(
        request=request,
        template_name='teachers/list.html',
        context={
            'title': 'List of Teachers',
            'teachers': teachers,
        }
    )


def detail_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'teachers/detail.html', {'title': f'Detail of {teacher.first_name} {teacher.last_name}', 'teacher': teacher})


def create_teacher(request):
    if request.method == 'GET':
        form = CreateTeacherForm()
    elif request.method == 'POST':
        form = CreateTeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/teachers/')

    return render(
        request=request,
        template_name='teachers/create.html',
        context={
            'title': 'Create Teacher',
            'form': form,
        }
    )


def update_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'GET':
        form = UpdateTeacherForm(instance=teacher)
    elif request.method == 'POST':
        form = UpdateTeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            teacher.save()
            return HttpResponseRedirect('/teachers/')

    return render(
        request=request,
        template_name='teachers/create.html',
        context={
            'title': 'Update Teacher',
            'form': form,
        }
    )


def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return HttpResponseRedirect(reverse('teachers:list'))
    else:
        return render(request, 'teachers/delete.html', {'teacher': teacher})



