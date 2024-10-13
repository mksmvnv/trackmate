from django import forms
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _

from apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        base_widget_attrs = {
            "class": "form-control mb-2 mt-2",
        }

        fields = ["title", "description", "priority", "completed_by"]
        labels = {
            "title": _("Название"),
            "description": _("Описание"),
            "priority": _("Приоритет"),
            "completed_by": _("Выполнить до:"),
        }
        widgets = {
            "title": forms.TextInput(
                attrs={
                    **base_widget_attrs,
                    "style": "width: 100%; height: 40px;",
                    "placeholder": _("Введите название задачи"),
                }
            ),
            "description": forms.Textarea(
                attrs={
                    **base_widget_attrs,
                    "style": "width: 100%; height: 60px;",
                    "placeholder": _("Введите описание задачи"),
                }
            ),
            "priority": forms.Select(
                attrs={
                    **base_widget_attrs,
                    "style": "width: 100%; height: 40px;",
                }
            ),
            "completed_by": forms.DateTimeInput(
                attrs={
                    **base_widget_attrs,
                    "style": "width: 100%; height: 40px;",
                    "type": "datetime-local",
                },
            ),
        }
