from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_created=True)
    deadline = models.DateTimeField()
    checker = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag")

    class Meta:
        ordering = ["-created_at", "-checker"]



class Tag(models.Model):
    name = models.CharField(max_length=255)
