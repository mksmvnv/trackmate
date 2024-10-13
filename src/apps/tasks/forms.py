from django import forms
from django.utils.translation import gettext_lazy as _

from apps.tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        base_widget_attrs = {
            "class": "form-control mb-2 mt-2",
        }

        fields = ["title", "description", "completed_by", "priority"]
        labels = {
            "title": _("Название"),
            "description": _("Описание"),
            "completed_by": _("Дата выполнения"),
            "priority": _("Приоритет"),
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
            "completed_by": forms.DateInput(
                attrs={
                    **base_widget_attrs,
                    "style": "width: 100%; height: 40px;",
                    "placeholder": _("Введите дату выполнения задачи"),
                }
            ),
            "priority": forms.Select(
                attrs={
                    **base_widget_attrs,
                    "style": "width: 100%; height: 40px;",
                }
            ),
        }
