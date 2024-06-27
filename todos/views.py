""" login, register and all task views """
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.http import Http404
from todos.serializers import TodoItemSerializer
from todos.models import Todos

class loginView(ObtainAuthToken):
    """ login with user data """
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
    """ all task views """
    authentication_classes = [TokenAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request, pk=None, format=None):
        """ get one or all tasks from db """
        if pk:
            todo = self.get_object(pk)
            serializer = TodoItemSerializer(todo)
            return Response(serializer.data)
        else:
            todos = Todos.objects.all()
            serializer = TodoItemSerializer(todos, many=True)
            return Response(serializer.data)
    def post(self, request, format=None):
        """ create a new task """
        data = request.data.copy()
        serializer = TodoItemSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk, format=None):
        """ overwrite an existing task """
        todo = self.get_object(pk)
        data = request.data.copy()
        serializer = TodoItemSerializer(todo, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk, format=None):
        """ delete an existing task """
        todo = self.get_object(pk)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    def get_object(self, pk):
        """ get an object from db """
        try:
            return Todos.objects.get(pk=pk)
        except Todos.DoesNotExist:
            raise Http404
