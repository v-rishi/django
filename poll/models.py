from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
"""
This app will have 2 models - a Question model and a 
Choices model. The Choices model will reference the Question model.
"""


class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1)<=self.pub_date<=timezone.now()


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

