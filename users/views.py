from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login

from users.forms import UserCreationForm


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
