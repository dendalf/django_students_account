
from django.contrib import admin
from django.urls import path
from students.views import index, create_student, update_student
from students.views import get_students


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('students/', get_students),
    path('students/create/', create_student),
    path('students/update/<int:pk>/', update_student),
]
