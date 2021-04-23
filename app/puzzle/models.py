from django.db import models
from django.conf import settings


class Word(models.Model):
    """Word object"""
    word = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.word


class Category(models.Model):
    """Category object"""
    category = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.category


class Group(models.Model):
    """Group object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    group = models.CharField(max_length=255)
    categories = models.ManyToManyField("Category")
    words = models.ManyToManyField("Word")

    def __str__(self):
        return self.group


class Puzzle(models.Model):
    """Puzzle object"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    puzzle = models.CharField(max_length=255)
    groups = models.ManyToManyField("Group")

    def __str__(self):
        return self.puzzle
