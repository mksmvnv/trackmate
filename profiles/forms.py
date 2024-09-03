from django import forms
from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["bio", "avatar", "first_name", "last_name", "gender", "age"]
        labels = {
            "bio": "О себе",
            "avatar": "Аватар",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "gender": "Пол",
            "age": "Возраст",
        }
        widgets = {
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 60px;",
                    "placeholder": "О себе",
                }
            ),
            "avatar": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Имя",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Фамилия",
                }
            ),
            "gender": forms.Select(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Возраст",
                }
            ),
        }
