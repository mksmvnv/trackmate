from django.urls import reverse_lazy
from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.db.models.query import QuerySet

from .models import Task
from .forms import TaskForm


class CreateTaskListView(CreateView, ListView):
    """Add and list tasks"""

    template_name = "index.html"

    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("index")

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
        return Task.objects.all().order_by("created_at")

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


class UpdateTaskView(UpdateView):
    """Update task"""

    model = Task
    form_class = TaskForm
    template_name = "update.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return self.render_to_response(self.get_context_data(form=form))


class DeleteTaskView(DeleteView):
    """Delete task"""

    model = Task
    success_url = reverse_lazy("index")

    def get(self, request, *args, **kwargs) -> HttpResponse:
        return self.post(request, *args, **kwargs)
