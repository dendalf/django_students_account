from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.middleware.csrf import get_token
from django.shortcuts import render, get_object_or_404

from webargs.djangoparser import use_args
from webargs.fields import Str

from .forms import CreateStudentForm, UpdateStudentForm
from .models import Student
from .utils import format_list_students


def index(request):
    return HttpResponse('Welcome to LMS')


@use_args(
    {
        'first_name': Str(required=False),
        'last_name': Str(required=False),
    },
    location='query',

)
def get_students(request, args):
    students = Student.objects.all().order_by('birthdate')

    if len(args) and (args.get('first_name') or args.get('last_name')):
        students = students.filter(
            Q(first_name__istartswith=args.get('first_name', '')) | Q(last_name__istartswith=args.get('last_name', ''))
        )

    form = '''
        <form method="get">
          <label for="fname">First name:</label><br>
          <input type="text" id="fname" name="first_name"><br>
          <label for="lname">Last name:</label><br>
          <input type="text" id="lname" name="last_name"><br><br>
          <input type="submit" value="Submit">
        </form> 
    
    '''

    string = form + format_list_students(students)
    response = HttpResponse(string)
    return response


def create_student(request):
    if request.method == 'GET':
        form = CreateStudentForm()
    elif request.method == 'POST':
        form = CreateStudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/students/')

    token = get_token(request)
    html_form = f'''      
            <form method="post">
            <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
              <table>
              {form.as_table()}
              </table>
              <input type="submit" value="Submit">
            </form>
        '''

    return HttpResponse(html_form)


# def update_student(request, pk):
#     students = Student.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = get_object_or_404(UpdateStudentForm)
#     elif request.method == 'POST':
#         form = get_object_or_404(UpdateStudentForm)
#         if form.is_valid():
#             # students.update(form)
#             # print(form)
#             return HttpResponseRedirect('/students/')
#
#     token = get_token(request)
#     html_form = f'''
#             <form method="post">
#             <input type="hidden" name="csrfmiddlewaretoken" value="{token}">
#               <table>
#               {form.as_table()}
#               </table>
#               <input type="submit" value="Submit">
#             </form>
#         '''
#
#     return HttpResponse(html_form)
