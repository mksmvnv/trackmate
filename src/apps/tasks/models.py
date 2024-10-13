from django.db import models
from django.utils.timezone import now

from django.conf import settings
from django.utils.translation import gettext_lazy as _

from django_enumfield import enum


class Priority(enum.Enum):
    Default = 0
    Low = 1
    Normal = 2
    High = 3

    __labels__ = {
        0: _("Не указан"),
        1: _("Низкий"),
        2: _("Нормальный"),
        3: _("Высокий"),
    }


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2056, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    completed_by = models.DateTimeField(default=now)
    priority = enum.EnumField(Priority, default=Priority.Default)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )

    class Meta:
        db_table = "tasks"
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return (
            f"{self.title} - {self.user} - {self.created_at.strftime('%H:%M %d-%m-%Y')}"
        )
