
from django.contrib import admin
from django.urls import path

from groups.views import get_groups, detail_group, create_group, update_group
from students.views import index, create_student, update_student, detail_student, get_students
from teachers.views import get_teachers, create_teacher, update_teacher, detail_teacher

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student),
    path('students/update/<int:pk>/', update_student),
    path('students/detail/<int:pk>/', detail_student),
    path('groups/', get_groups),
    path('groups/create/', create_group),
    path('groups/update/<int:pk>/', update_group),
    path('groups/detail/<int:pk>/', detail_group),
    path('teachers/', get_teachers),
    path('teachers/create/', create_teacher),
    path('teachers/update/<int:pk>/', update_teacher),
    path('teachers/detail/<int:pk>/', detail_teacher),
]
