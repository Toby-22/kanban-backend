from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from scrum_board_backend.serializers import TodoItemSerializer
from todos.models import Todos
from rest_framework.authtoken.models import Token
from django.http import Http404
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class loginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class TodoItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        if pk:
            todo = self.get_object(pk)
            serializer = TodoItemSerializer(todo)
            return Response(serializer.data)
        else:
            todos = Todos.objects.all()
            serializer = TodoItemSerializer(todos, many=True)
            return Response(serializer.data)
    
    def post(self, request, format=None):
        data = request.data.copy()
        if 'assignee' not in data:
            data['assignee'] = request.user.id
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def put(self, request, pk, format=None):
        todo = self.get_object(pk)
        data = request.data.copy()
        if 'assignee' not in data:
            data['assignee'] = request.user.id
        serializer = TodoItemSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
    def get_object(self, pk):
        try:
            return Todos.objects.get(pk=pk)
        except Todos.DoesNotExist:
            raise Http404