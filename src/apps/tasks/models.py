import uuid

from django.db import models
from django.utils.timezone import now

from django.conf import settings

from django_enumfield import enum


class Priority(enum.Enum):
    Low = 1
    Normal = 2
    High = 3

    __labels__ = {
        1: "Низкий",
        2: "Обычный",
        3: "Высокий",
    }


class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2056, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
    priority = enum.EnumField(enum=Priority, default=Priority.Normal)
    completed_by = models.DateTimeField(default=now)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="tasks"
    )

    class Meta:
        db_table = "tasks"
        verbose_name = "task"
        verbose_name_plural = "tasks"
        ordering = ["id"]

    def __str__(self):
        return (
            f"{self.title} - {self.user} - {self.created_at.strftime('%d-%m-%Y %H:%M')}"
        )
