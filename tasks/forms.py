from django import forms
from django.utils.translation import gettext_lazy as _

from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        labels = {"title": _("Название"), "description": _("Описание")}
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": _("Введите название задачи"),
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 60px;",
                    "placeholder": _("Введите описание задачи"),
                }
            ),
        }
