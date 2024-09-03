from django.urls import reverse_lazy
from django.http import HttpResponse    
from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

from profiles.models import Profile
from profiles.forms import ProfileForm


class ProfileView(LoginRequiredMixin, TemplateView):
    """Profile page"""
    template_name = "profile.html"
    login_url = reverse_lazy("login")


class EditProfileView(LoginRequiredMixin, UpdateView):
    """Edit profile"""
    template_name = "edit_profile.html"
    model = Profile
    form_class = ProfileForm
    login_url = reverse_lazy("login")

    def get_success_url(self):
        return reverse_lazy("profile", kwargs={"id": self.request.user.profile.id})

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    
    def form_invalid(self, form):
        return super().form_invalid(form)
