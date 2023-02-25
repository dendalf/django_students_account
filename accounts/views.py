from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordResetView, \
    PasswordResetConfirmView, PasswordChangeDoneView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views.generic.edit import ProcessFormView

from accounts.forms import UserRegisterForm, UserPasswordChangeForm, UserUpdateForm, ProfileUpdateForm


class AccountRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('home')
    template_name = 'accounts/register.html'


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountChangePasswordView(PasswordChangeView):
    model = User
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('accounts:change_done')
    template_name = 'accounts/password_change.html'


class AccountChangeDoneView(PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html')


class UpdateProfileView(LoginRequiredMixin, ProcessFormView):
    def get(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user)
        profile_form = ProfileUpdateForm(instance=profile)

        return render(request, 'accounts/update.html', {'user_form': user_form, 'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user = request.user
        profile = user.profile
        user_form = UserUpdateForm(instance=user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=profile, data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

        return HttpResponseRedirect(reverse('accounts:profile'))


# class AccountResetPasswordView(PasswordResetView):
#     model = User
#     form_class = UserResetPasswordForm
#     success_url = reverse_lazy('accounts:password_reset_confirm')
#     template_name = 'accounts/password_reset_form.html'
#
#
# class AccountResetConfirmView(PasswordResetConfirmView):
#     model = User
#     form_class = UserResetConfirm
#     success_url = reverse_lazy('home')
#     template_name = 'accounts/register.html'
