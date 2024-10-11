from django.urls import reverse_lazy
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from apps.profiles.models import Profile
from apps.profiles.forms import ProfileForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Profile page"""

    template_name = "profile.html"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        user = self.request.user
        total_tasks = user.tasks.count()
        completed_tasks = user.tasks.filter(status=True).count()

        if total_tasks > 0:
            completion_percentage = int((completed_tasks / total_tasks) * 100)
        else:
            completion_percentage = 0

        context["total_tasks"] = total_tasks
        context["completed_tasks"] = completed_tasks
        context["completion_percentage"] = completion_percentage

        return context


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
