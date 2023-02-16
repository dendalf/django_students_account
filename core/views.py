from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404


# Create your views here.
from django.urls import reverse


def index(request):
    return render(request, 'index.html')


class CustomUpdateBaseView:
    model = None
    form_class = None
    success_url = None
    template_name = None

    @classmethod
    def update(cls, request, pk):
        student = get_object_or_404(cls.model, pk=pk)
        if request.method == 'GET':
            form = cls.form_class(instance=student)
        elif request.method == 'POST':
            form = cls.form_class(request.POST, instance=student)
            if form.is_valid():
                student.save()
                return HttpResponseRedirect(reverse(cls.success_url))

        return render(
            request=request,
            template_name=cls.template_name,
            context={
                'title': 'Update Student',
                'form': form,
            }
        )