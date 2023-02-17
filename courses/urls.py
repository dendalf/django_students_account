
from django.urls import path

from .views import get_course, CreateCourseView, UpdateCourseView, DeleteCourseView

app_name = 'courses'

urlpatterns = [
    path('', get_course, name='list'),
    path('create/', CreateCourseView.as_view(), name='create'),
    path('update/<int:pk>/', UpdateCourseView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteCourseView.as_view(), name='delete'),
]
