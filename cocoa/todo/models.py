from django.db import models

# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200, null=False,
    help_text="입력")
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.task
