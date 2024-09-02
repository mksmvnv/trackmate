from django.db import models
from django.utils.timezone import now

from django.conf import settings


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2056, null=True, blank=True)
    status = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=now)
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
