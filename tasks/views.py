from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import (
    TemplateView,
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404

from tasks.models import Task
from tasks.forms import TaskForm


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

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)

        task_list = self.get_queryset()
        paginator = Paginator(task_list, self.paginate_by)
        page_number = self.request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj

        return context

    def get_queryset(self) -> QuerySet:
        return Task.objects.filter(user=self.request.user).order_by("created_at")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)


class UpdateTaskStatusView(LoginRequiredMixin, UpdateView):
    """Update task status"""

    model = Task
    fields = ["status"]
    login_url = reverse_lazy("login")

    def get_object(self, queryset=None):
        return get_object_or_404(Task, id=self.kwargs["pk"], user=self.request.user)

    def form_valid(self, form: BaseModelForm) -> JsonResponse:
        form.instance.status = self.request.POST.get("status") == "true"
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

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return self.post(request, *args, **kwargs)
