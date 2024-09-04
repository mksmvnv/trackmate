from django import forms
from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            "image",
            "first_name",
            "last_name",
            "profession",
            "location",
            "bio",
            "gender",
            "age",
        ]
        labels = {
            "image": "Фото профиля",
            "first_name": "Имя",
            "last_name": "Фамилия",
            "profession": "Профессия",
            "location": "Местоположение",
            "bio": "О себе",
            "gender": "Пол",
            "age": "Возраст",
        }
        widgets = {
            "image": forms.FileInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Введите имя",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Введите фамилию",
                }
            ),
            "profession": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Введите профессию",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": "Введите местоположение",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 60px;",
                    "placeholder": "О себе",
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
                    "placeholder": "Введите возраст",
                }
            ),
        }
