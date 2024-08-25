from django.db import models
from django.utils.timezone import now


class Task(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2056, null=True, blank=True)
    status = models.BooleanField(default=False)
    сreated_at = models.DateTimeField(default=now)

    class Meta:
        db_table = "tasks"
        verbose_name = "task"
        verbose_name_plural = "tasks"

    def __str__(self):
        return f"{self.title} <{self.сreated_at.strftime('%d-%m-%Y %H:%M')}>"
