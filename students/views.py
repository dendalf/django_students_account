from django.http import HttpResponse
from django.shortcuts import render

from .models import Student


def index(request):
    students = Student.objects.all().order_by('birthdate')
    # string = '<br>'.join(str(student) for student in students)
    string = '<table><thead><tr><th>First name</th><th>Last name</th><th>Email</th><th>Birthdate</th></thead><tbody>'
    for st in students:
        string += f'<tr><td>{st.first_name} </td><td>{st.last_name} </td><td>{st.email} </td><td>{st.birthdate} </td></tr>'
    string += '</tbody></table>'
    return HttpResponse(string)

