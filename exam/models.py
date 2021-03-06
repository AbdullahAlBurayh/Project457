from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class ExamSetManager(models.Manager):
    def create_examset(self, exam, user, marks):
        examset = self.create(
            exam=exam,
            user=user,
            marks=marks
        )


class Question(models.Model):

    question = models.CharField(max_length=100)
    img = models.ImageField(blank=True)
    optionA = models.CharField(max_length=100)
    optionB = models.CharField(max_length=100)
    optionC = models.CharField(max_length=100)
    optionD = models.CharField(max_length=100)
    answer = models.CharField(max_length=200)
    hint = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.question} \t\t Options: \nA. {self.optionA} \nB.{self.optionB} \nC.{self.optionC} \nD.{self.optionD} '


class Exam(models.Model):
    examid = models.AutoField(primary_key=True, default=None)
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    totalMarks = models.IntegerField()
    questions = models.ManyToManyField(Question)
    practice = models.BooleanField(default=False)

    def __str__(self):
        return f'{name}'


class ExamSet(models.Model):
    exam = models.ForeignKey(Exam, db_column='examid',
                             on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    marks = models.IntegerField(default=0)
    objects = ExamSetManager()
