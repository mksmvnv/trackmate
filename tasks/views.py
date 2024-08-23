from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView

from .models import Task
from .forms import TaskForm


class CreateTaskListView(CreateView, ListView):
    """Add and list tasks"""

    template_name = "index.html"

    model = Task
    form_class = TaskForm
    success_url = "/"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_valid(form)

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)


class UpdateTaskStatusView(UpdateView):
    """Update task status"""

    model = Task
    fields = ["status"]

    def form_valid(self, form: BaseModelForm) -> JsonResponse:
        form.instance.status = self.request.POST.get("status") == "true"
        self.object = form.save()
        return JsonResponse({"success": True})

    def form_invalid(self, form: BaseModelForm) -> JsonResponse:
        return JsonResponse({"success": False, "errors": form.errors}, status=400)
