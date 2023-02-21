
from django.contrib import admin
from django.urls import path, include

from core.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/',  include('accounts.urls')),
    path('', index, name='home'),
    path('students/', include('students.urls')),
    path('groups/', include('groups.urls')),
    path('teachers/', include('teachers.urls')),
    path('courses/', include('courses.urls')),
]
