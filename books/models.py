from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=128)
    authors = models.ManyToManyField("users.User", related_name="books")
