from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from users.validators import validate_no_cyrillic

User = get_user_model()


class UserCreationForm(UserCreationForm):
    usable_password = None

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                "autocomplete": "email",
                "class": "form-control",
                "placeholder": "Введите email",
            }
        ),
    )

    username = forms.CharField(
        label="Логин",
        max_length=150,
        widget=forms.TextInput(
            attrs={
                "autocomplete": "username",
                "class": "form-control",
                "placeholder": "Введите логин",
            }
        ),
        validators=[validate_no_cyrillic],
    )

    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Введите пароль",
            }
        ),
    )

    password2 = forms.CharField(
        label="Повторите пароль",
        widget=forms.PasswordInput(
            attrs={
                "autocomplete": "new-password",
                "class": "form-control",
                "placeholder": "Подтвердите пароль",
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "email")
