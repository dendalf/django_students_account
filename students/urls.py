
from django.urls import path

from .views import create_student, update_student, detail_student, get_students, delete_student, UpdateStudent, \
    UpdateStudentView

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    # path('update/<int:pk>/', UpdateStudent.update, name='update'),  # custom view
    path('update/<int:pk>/', UpdateStudentView.as_view(), name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]
