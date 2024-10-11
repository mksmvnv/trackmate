from django.views import View
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.views import (
    LoginView,
    PasswordResetView,
    PasswordResetConfirmView,
)

from apps.users.forms import (
    UserCreationForm,
    CustomAuthenticationForm,
    CustomPasswordResetForm,
    CustomSetPasswordForm,
)


class RegisterView(View):
    """Register new user"""

    template_name = "registration/register.html"

    def get(self, request) -> HttpResponse:
        context = {
            "form": UserCreationForm(),
        }
        return render(request, self.template_name, context)

    def post(self, request) -> HttpResponse:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("index")

        context = {"form": form}
        return render(request, self.template_name, context)


class CustomLoginView(LoginView):
    """Login user"""

    form_class = CustomAuthenticationForm
    template_name = "registration/login.html"


class CustomPasswordResetView(PasswordResetView):
    """Reset user password"""

    form_class = CustomPasswordResetForm
    template_name = "registration/password_reset_form.html"


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """Confirm reset user password"""

    form_class = CustomSetPasswordForm
    template_name = "registration/password_reset_confirm.html"

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["uid"] = self.kwargs["uidb64"]
        context["token"] = self.kwargs["token"]
        return context
