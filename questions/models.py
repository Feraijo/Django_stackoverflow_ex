import datetime
from django.db import models
from django.utils import timezone

class Question(models.Model):
    def __str__(self):
        return self.question_text    
    question_text = models.TextField(blank=True)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField('date published')
    has_answer = models.BooleanField(default=False)

class Answer(models.Model):
    def __str__(self):
        return self.answer_text
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField(default=None, blank=True, null=True, name='date answered')
    is_accepted = models.BooleanField(default=False)
    def accept(self):
        self.is_accepted = True
        self.question.has_answer = True           