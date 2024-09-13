from django import forms
from django.utils.translation import gettext_lazy as _

from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    clear_image = forms.BooleanField(
        required=False,
        label=_("Удалить текущее изображение"),
        widget=forms.CheckboxInput(
            attrs={
                "class": "form-check-input",
                "style": "width: 20px; height: 20px;",
            }
        ),
    )

    class Meta:
        model = Profile
        fields = [
            "image",
            "clear_image",
            "first_name",
            "last_name",
            "profession",
            "location",
            "bio",
            "gender",
            "age",
        ]
        labels = {
            "image": _("Фото профиля"),
            "first_name": _("Имя"),
            "last_name": _("Фамилия"),
            "profession": _("Профессия"),
            "location": _("Местоположение"),
            "bio": _("О себе"),
            "gender": _("Пол"),
            "age": _("Возраст"),
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
                    "placeholder": _("Введите имя"),
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": _("Введите фамилию"),
                }
            ),
            "profession": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": _("Введите профессию"),
                }
            ),
            "location": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 40px;",
                    "placeholder": _("Введите местоположение"),
                }
            ),
            "bio": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "style": "width: 100%; height: 60px;",
                    "placeholder": _("О себе"),
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
                    "placeholder": _("Введите возраст"),
                }
            ),
        }

    def save(self, commit=True):
        profile = super().save(commit=False)

        if self.cleaned_data.get("clear_image"):
            profile.image = f"profile_images/default/user_{profile.user.id}/default_profile_image_user_{profile.user.id}.png"

        if commit:
            profile.save()

        return profile
