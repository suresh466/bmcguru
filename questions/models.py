from django.db import models

# Create your models here.

class Question(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated= models.DateTimeField(auto_now=True)
    question_num = models.PositiveIntegerField(editable=False)
    question = models.TextField(max_length=500,blank=False)
    opt_a = models.CharField(max_length=255,blank=False)
    opt_b = models.CharField(max_length=255,blank=False)
    opt_c = models.CharField(max_length=255,blank=False)
    opt_d = models.CharField(max_length=255,blank=False)
    answer = models.CharField(max_length=1,blank=False)
    #hint = models.CharField(max_length=500,blank=True)
    right_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    wrong_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    total_right_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)
    total_wrong_count = models.PositiveIntegerField(
            default=0,blank=False,editable=False)

    def __str__(self):
        return str(self.pk)

class Info(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    total_questions = models.PositiveIntegerField(blank=False,default=0)
    last_answered = models.PositiveIntegerField(blank=False,default=0)
    iteration_num = models.PositiveIntegerField(default=1,blank=False,editable=False)
    identifier = models.PositiveIntegerField(default=1,blank=False,editable=False)

    def __str__(self):
        return str(self.total_questions)
