import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy


def validate_no_cyrillic(value):
    if re.search(r"[А-Яа-яЁё]", value):
        raise ValidationError(
            gettext_lazy("Логин может содержать только латинские буквы"),
            params={"value": value},
        )
