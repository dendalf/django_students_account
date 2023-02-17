from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from webargs.djangoparser import use_args
from webargs.fields import Str

from students.models import Student
from .forms import CreateGroupForm, UpdateGroupForm
from .models import Group


@use_args(
    {
        'group_name': Str(required=False),
    },
    location='query',

)
def get_groups(request, args):
    groups = Group.objects.all().order_by('start_date')

    if len(args) and (args.get('group_name')):
        groups = groups.filter(
            Q(group_name__istartswith=args.get('group_name', ''))
        )

    return render(
        request=request,
        template_name='groups/list.html',
        context={
            'title': 'List of Groups',
            'groups': groups,
        }
    )


def detail_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    return render(request, 'groups/detail.html', {'title': f'Detail of {group.group_name}', 'group': group})


def create_group(request):
    if request.method == 'GET':
        form = CreateGroupForm()
    elif request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/create.html',
        context={
            'title': 'Create Group',
            'form': form,
        }
    )


def update_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    students = {'students': Student.objects.filter(group=group)}
    if request.method == 'GET':
        form = UpdateGroupForm(instance=group, initial=students)
    elif request.method == 'POST':
        form = UpdateGroupForm(request.POST, instance=group, initial=students)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('groups:list'))

    return render(
        request=request,
        template_name='groups/update.html',
        context={
            'title': 'Update Group',
            'form': form,
            'group': group,
        }
    )


def delete_group(request, pk):
    group = get_object_or_404(Group, pk=pk)
    if request.method == 'POST':
        group.delete()
        return HttpResponseRedirect(reverse('groups:list'))
    else:
        return render(request, 'groups/delete.html', {'group': group})




