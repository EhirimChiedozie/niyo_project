from django.db import models
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class Task(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=100)
    status = models.CharField(max_length=100)

    def __str__(self):
        return self.title