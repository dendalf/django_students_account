
from django.urls import path

from .views import AccountRegisterView, AccountLoginView, AccountLogoutView, AccountChangePasswordView, \
    AccountChangeDoneView, profile_view, UpdateProfileView

app_name = 'accounts'

urlpatterns = [
    path('register/', AccountRegisterView.as_view(), name='register'),
    path('login/', AccountLoginView.as_view(), name='login'),
    path('logout/', AccountLogoutView.as_view(), name='logout'),
    path('password_change/', AccountChangePasswordView.as_view(), name='password_change'),
    path('password_change_done/', AccountChangeDoneView.as_view(), name='change_done'),
    path('profile/', profile_view, name='profile'),
    path('profile/update/', UpdateProfileView.as_view(), name='profile_update')
    # path('password_reset/', AccountResetPasswordView.as_view(), name='password_reset'),
    # path('reset_confirm/', AccountResetConfirmView.as_view(), name='password_reset_confirm'),
]
