from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Profile
from profiles.forms import ProfileForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Profile page"""

    template_name = "profile.html"
    login_url = reverse_lazy("login")


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile"""

    template_name = "profile_update.html"
    model = Profile
    form_class = ProfileForm
    login_url = reverse_lazy("login")

    def get_success_url(self) -> str:
        return reverse_lazy("profile", kwargs={"id": self.request.user.profile.id})

    def get_object(self, queryset=None) -> Profile:
        return get_object_or_404(Profile, user=self.request.user)

    def form_valid(self, form: ProfileForm) -> HttpResponse:
        form.save()
        return super().form_valid(form)
