from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description"]
        labels = {"title": "Название", "description": "Описание"}
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Введите название задачи",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 60px;",
                    "placeholder": "Введите описание задачи",
                }
            ),
        }
