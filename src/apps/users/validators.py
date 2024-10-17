import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_no_cyrillic(value):
    if re.search(r"[А-Яа-яЁё]", value):
        raise ValidationError(
            _("Логин может содержать только латинские буквы"),
            params={"value": value},
        )
