from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordResetForm,
    SetPasswordForm,
)
from django.utils.translation import gettext_lazy as _

from apps.users.validators import validate_no_cyrillic

User = get_user_model()


class UserCreationForm(UserCreationForm):
    usable_password = None

    base_widget_attrs = {"class": "form-control mb-2 mt-2"}

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "email",
                "placeholder": _("Введите email"),
            }
        ),
    )

    username = forms.CharField(
        label=_("Логин"),
        max_length=150,
        widget=forms.TextInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "username",
                "placeholder": _("Введите логин"),
            }
        ),
        validators=[validate_no_cyrillic],
    )

    first_name = forms.CharField(
        label=_("Имя"),
        max_length=150,
        widget=forms.TextInput(
            attrs={
                **base_widget_attrs,
                "placeholder": _("Введите имя"),
            }
        ),
    )

    last_name = forms.CharField(
        label=_("Фамилия"),
        max_length=150,
        widget=forms.TextInput(
            attrs={
                **base_widget_attrs,
                "placeholder": _("Введите фамилию"),
            }
        ),
    )

    password1 = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "new-password",
                "placeholder": _("Введите пароль"),
            }
        ),
    )

    password2 = forms.CharField(
        label=_("Повторите пароль"),
        widget=forms.PasswordInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "new-password",
                "placeholder": _("Подтвердите пароль"),
            }
        ),
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ("username", "first_name", "last_name", "email")


class CustomAuthenticationForm(AuthenticationForm):

    base_widget_attrs = {"class": "form-control mb-2 mt-2"}

    username = forms.CharField(
        label=_("Логин"),
        widget=forms.TextInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "username",
                "placeholder": _("Введите логин"),
            }
        ),
        validators=[validate_no_cyrillic],
    )

    password = forms.CharField(
        label=_("Пароль"),
        widget=forms.PasswordInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "current-password",
                "placeholder": _("Введите пароль"),
            }
        ),
    )


class CustomPasswordResetForm(PasswordResetForm):

    base_widget_attrs = {"class": "form-control mb-2 mt-2"}

    email = forms.EmailField(
        label="Email",
        max_length=254,
        widget=forms.EmailInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "email",
                "placeholder": _("Введите email"),
            }
        ),
    )


class CustomSetPasswordForm(SetPasswordForm):

    base_widget_attrs = {"class": "form-control mb-2 mt-2"}

    new_password1 = forms.CharField(
        label=_("Новый пароль"),
        widget=forms.PasswordInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "new-password",
                "placeholder": _("Введите новый пароль"),
            }
        ),
    )

    new_password2 = forms.CharField(
        label=_("Повторите новый пароль"),
        widget=forms.PasswordInput(
            attrs={
                **base_widget_attrs,
                "autocomplete": "new-password",
                "placeholder": _("Подтвердите новый пароль"),
            }
        ),
    )
