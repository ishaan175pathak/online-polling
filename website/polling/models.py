from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    
    user = models.CharField(max_length=100, blank=False)
    question = models.CharField(max_length=1000, blank=False)
    options1 = models.CharField(max_length=100, blank=False)
    options2 = models.CharField(max_length=100, blank=False)
    options3 = models.CharField(max_length=100, blank=False)
    options4 = models.CharField(max_length=100, blank=False)
    answered_by = models.CharField(max_length=100, blank=True)
    choice = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(blank=True)

    def __str__(self) -> str:
        return f"user - {self.user} | question - {self.question} | Options - {self.options1} {self.options2} {self.options3} {self.options4} | Date of Creation - {self.date} | Answered by - {self.answered_by} | Choice - {self.choice}"
