from rest_framework import serializers
from todos.models import Todos


 

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = '__all__'