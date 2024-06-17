from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from scrum_board_backend.serializers import TodoItemSerializer
from todos.models import Todos

class TodoItemView(APIView):
    def get(self, request, format=None):
        todos = Todos.objects.all()
        serializer = TodoItemSerializer(todos, many=True)
        return Response(serializer.data)
        