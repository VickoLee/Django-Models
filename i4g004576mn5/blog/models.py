from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()
# from datetime import datetime
# from django.contrib.auth.models import User

class Post(models.Model):
    Title = models.CharField(max_length=200)
    Text = models.CharField(max_length=5000)
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField()
    Published_date = models.DateTimeField()
