""" user serializer """
from rest_framework import serializers
from django.contrib.auth.models import User
class UserSerializer(serializers.ModelSerializer):
    """ user serializer """
    class Meta:
        """ user model """
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}
    def create(self, validated_data):
        """ create a new user """
        user = User.objects.create_user(**validated_data)
        return user
