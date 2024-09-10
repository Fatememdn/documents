from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
class UserRegister(ModelSerializer):
    class Meta:
        model = User
        fields = ['username','password','email', 'first_name', 'last_name'] 

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        exclude = ['password']