from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class QuestionManager(models.Manager):

    def new():
        pass

    def popular():
        pass


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey('User')
    likes = models.CharField(max_length=100)
    objects = QuestionManager()


class Answer(models.Model):
    text = models.CharField(max_length=255)
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question')
    author = models.ForeignKey('User')
