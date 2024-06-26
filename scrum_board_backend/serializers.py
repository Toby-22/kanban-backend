from rest_framework import serializers
from todos.models import Todos
from django.contrib.auth.models import User


 

class TodoItemSerializer(serializers.ModelSerializer):
    assignee = serializers.SlugRelatedField(slug_field='username', queryset=User.objects.all())

    class Meta:
        model = Todos
        fields = '__all__'