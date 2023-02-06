
from django.urls import path

from .views import get_teachers, create_teacher, update_teacher, detail_teacher, delete_teacher

app_name = 'teachers'

urlpatterns = [
    path('', get_teachers, name='list'),
    path('create/', create_teacher, name='create'),
    path('update/<int:pk>/', update_teacher, name='update'),
    path('detail/<int:pk>/', detail_teacher, name='detail'),
    path('delete/<int:pk>/', delete_teacher, name='delete'),
]
