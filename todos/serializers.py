""" this module is the todo serializer"""
from rest_framework import serializers
from django.contrib.auth.models import User
from todos.models import Todos


class TodoItemSerializer(serializers.ModelSerializer):
    """ This class is representing the todo Serializer """
    assignee = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())
    class Meta:
        """ ljlkjöljö """
        model = Todos
        fields = '__all__'
