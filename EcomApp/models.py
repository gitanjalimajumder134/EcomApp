from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

# class Users(AbstractUser):
#     name = models.CharField(max_length=255)
#     email = models.CharField(max_length=255, unique= True)
#     password = models.CharField(max_length=255)
#     username = models.CharField(max_length=100, default=email, null=True)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(max_length=251)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Category'

    def __str__(self):
        return str(self.name)

class Quizzes(models.Model):
    title = models.CharField(max_length=255, default='New Quiz', verbose_name='Quize Title')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default= 1)
    created = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Quiz'

    def __str__(self):
        return str(self.title)

class Updated(models.Model):
    updated = models.DateField(verbose_name='Last Updated', auto_now=True)

    class Meta:
        abstract = True
 

class Question(Updated):
    Scale = (
        (0, ('Fundamental')),
        (1, ('Beginner')),
        (2, ('Intermediate')),
        (3, ('Advanced')),
        (4, ('Expert')),
    )

    Type = (
        (0, ('Multiple Choice')),
    )
    quiz = models.ForeignKey(Quizzes, on_delete=models.CASCADE, related_name='question')
    technique = models.IntegerField(choices=Type, default=0, verbose_name='Type of Question')
    title = models.CharField(max_length=255, verbose_name='Title')
    difficulty = models.IntegerField(choices=Scale, default=0, verbose_name='Difficulty')
    created_at = models.DateField(auto_now_add=True, verbose_name='Date Created')
    is_active = models.BooleanField(default=False, verbose_name='Active Status')

    class Meta:
        ordering = ('id',)
        verbose_name = 'Question'

    def __str__(self):
        return str(self.title)

class Answer(Updated):
    category = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    answer_text = models.CharField(max_length=255, verbose_name='Answer Text')
    is_right = models.BooleanField(default=False)

    class Meta:
        ordering = ('id',)
        verbose_name = 'Answer'

    def __str__(self):
        return str(self.answer_text)