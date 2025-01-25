from django.urls import reverse_lazy
from django.utils.timezone import now
from django.forms import BaseModelForm
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from apps.tasks.models import Task
from apps.tasks.forms import TaskForm


class IndexView(TemplateView):
    """Index page"""

    template_name = "index.html"


class CreateTaskListView(LoginRequiredMixin, CreateView, ListView):
    """Add and list tasks"""

    template_name = "tasks.html"
    model = Task
    form_class = TaskForm
    login_url = reverse_lazy("login")
    success_url = reverse_lazy("tasks")
    paginate_by = 5

    def get_queryset(self) -> QuerySet:
        return Task.objects.filter(user=self.request.user).order_by("-created_at")

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context["form"] = self.get_form()
        context["now"] = now()
        return context

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        context = self.get_context_data(form=form)
        return self.render_to_response(context)


class UpdateTaskStatusView(LoginRequiredMixin, UpdateView):
    """Update task status"""

    model = Task
    fields = ["status"]
    login_url = reverse_lazy("login")

    def get_object(self, queryset=None) -> Task:
        return get_object_or_404(Task, id=self.kwargs["pk"], user=self.request.user)

    def form_valid(self, form: BaseModelForm) -> JsonResponse:
        self.object = form.save()
        return JsonResponse({"success": True})

    def form_invalid(self, form: BaseModelForm) -> JsonResponse:
        return JsonResponse({"success": False, "errors": form.errors}, status=400)


class UpdateTaskView(LoginRequiredMixin, UpdateView):
    """Update task"""

    template_name = "task_update.html"
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks")
    login_url = reverse_lazy("login")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))


class DeleteTaskView(LoginRequiredMixin, DeleteView):
    """Delete task"""

    model = Task
    success_url = reverse_lazy("tasks")
    login_url = reverse_lazy("login")

