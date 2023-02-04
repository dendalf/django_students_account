
from django.urls import path

from .views import create_student, update_student, detail_student, get_students, delete_student

app_name = 'students'

urlpatterns = [
    path('', get_students, name='list'),
    path('create/', create_student, name='create'),
    path('update/<int:pk>/', update_student, name='update'),
    path('detail/<int:pk>/', detail_student, name='detail'),
    path('delete/<int:pk>/', delete_student, name='delete'),
]