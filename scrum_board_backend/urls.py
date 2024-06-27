"""
URL configuration for scrum_board_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contacts.views import RegisterView, UserListView, UserDetailView
from todos.views import TodoItemView, loginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TodoItemView.as_view()),
    path('login/', loginView.as_view()),
    path('tasks/<int:pk>/', TodoItemView.as_view()),
    path('register/', RegisterView.as_view()),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
