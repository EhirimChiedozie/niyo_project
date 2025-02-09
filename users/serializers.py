from djoser.serializers import UserCreateSerializer
from django.contrib.auth.models import User

class MyUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'username', 'password']