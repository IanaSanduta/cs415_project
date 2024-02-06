from rest_framework import serializers
from cs415.models import User, Expenses, Savings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'