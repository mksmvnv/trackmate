from django import forms
from profiles.models import Profile


class ProfileForm(forms.ModelForm):
    clear_image = forms.BooleanField(
        required=False,
        label="Удалить текущее изображение",
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

        def save(self, commit=True):
            profile = super().save(commit=False)

            if self.cleaned_data.get("clear_image"):
                profile.image.delete(save=False)
                profile.image = f"profile_images/default_profile_image_user_{profile.user.id}.png"  # Set the default image

            if commit:
                profile.save()

            return profile
