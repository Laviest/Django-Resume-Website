from django.db import models
from django.contrib.auth.models import User
from django.forms import Textarea

# Create your models here.


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="question_search", null=True)
    name = models.CharField(max_length=300, default='.')

    def __str__(self):
        return self.name

