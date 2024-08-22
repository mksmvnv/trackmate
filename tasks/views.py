from django.views.generic import ListView

from .models import Task


class IndexView(ListView):
    template_name = "index.html"

    model = Task
    queryset = Task.objects.all()
