from django.db import models

# Create your models here.
"""
This app will have 2 models - a Question model and a 
Choices model. The Choices model will reference the Question model.
"""

class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question_text


class Choices(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

