
from django.urls import path

from .views import get_groups, detail_group, create_group, update_group, delete_group

app_name = 'groups'

urlpatterns = [
    path('', get_groups, name='list'),
    path('create/', create_group, name='create'),
    path('update/<int:pk>/', update_group, name='update'),
    path('detail/<int:pk>/', detail_group, name='detail'),
    path('delete/<int:pk>/', delete_group, name='delete'),
]
