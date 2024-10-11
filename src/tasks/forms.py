from django import forms
from django.utils.translation import gettext_lazy as _

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task

        base_widget_attrs = {
            "class": "form-control mb-2 mt-2",
        }

        fields = ["title", "description"]
        labels = {"title": _("Название"), "description": _("Описание")}
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
        }
