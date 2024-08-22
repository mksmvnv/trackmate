from django.db import models


class Task(models.Model):
    class Meta:
        db_table = "tasks"
        verbose_name = "task"
        verbose_name_plural = "tasks"

    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2056)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.title
