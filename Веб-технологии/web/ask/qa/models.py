from __future__ import unicode_literals

from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class QuestionManager(models.Manager):

    def new(self):
        return Question.objects.order_by('-added_at')

    def popular(self):
        return Question.objects.order_by('-rating')


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)
    author = models.ForeignKey(User, related_name='question_author', default=1)
    likes = models.ManyToManyField(User, related_name='question_likes')
    objects = QuestionManager()

    def __unicode__(self):
        return self.title


class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey('Question')
    author = models.ForeignKey(User, related_name='answer_author')

    def __unicode__(self):
        return self.text
