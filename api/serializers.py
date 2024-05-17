from rest_framework import serializers
from users.models import Task
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'creator', 'title', 'description', 'created_at', 'due_date', 'priority', 'status']