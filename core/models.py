from django.db import models


class Task(models.Model):
    content = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_created=True)
    deadline = models.DateTimeField()
    checker = models.BooleanField()
    tags = models.ForeignKey("Tag", on_delete=models.SET_NULL)


class Tag(models.Model):
    name = models.CharField(max_length=255)
