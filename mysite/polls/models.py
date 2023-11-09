from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=255)
    # Add other fields for test information

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    # Add other fields for answers (e.g., question, is_correct)
