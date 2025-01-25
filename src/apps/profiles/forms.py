from django import forms

from apps.profiles.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        base_widget_attrs = {
            "class": "form-control mb-2 mt-2",
            "style": "width: 100%; height: 40px;",
        }

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
                    **base_widget_attrs,
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    **base_widget_attrs,
                    "placeholder": "Введите имя",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    **base_widget_attrs,
                    "placeholder": "Введите фамилию",
                }
            ),
            "profession": forms.TextInput(
                attrs={
                    **base_widget_attrs,
                    "placeholder": "Введите профессию",
                }
            ),
            "location": forms.TextInput(
                attrs={
                    **base_widget_attrs,
                    "placeholder": "Введите местоположение",
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control mb-2 mt-2",
                    "style": "width: 100%; height: 60px;",
                    "placeholder": "О себе",
                }
            ),
            "gender": forms.Select(
                attrs={
                    **base_widget_attrs,
                }
            ),
            "age": forms.NumberInput(
                attrs={
                    **base_widget_attrs,
                    "placeholder": "Введите возраст",
                }
            ),
        }


    
