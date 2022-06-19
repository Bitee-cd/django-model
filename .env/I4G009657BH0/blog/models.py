from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model

# Create your models here.
User = get_user_model()


class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default=datetime.today, blank=True)
    Published_date = models.DateTimeField(default=datetime.today, blank=True)

    def __str__(self) -> str:
        return self.Title
