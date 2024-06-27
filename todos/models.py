""" task model """
import datetime
from django.db import models
from django.contrib.auth.models import User


class Todos(models.Model):
    """ task model """
    STATUS = [
        ('todo', 'todo'),
        ('inWork', 'inWork'),
        ('inReview', 'inReview'),
        ('done', 'done'),
    ]
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    created_at = models.DateField(default=datetime.date.today)
    due_date = models.DateField(null=True, blank=True)
    assignee = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='todo', max_length=30)
    category = models.CharField(max_length=30, null=True, blank=True)
    def __str__(self):
        return f'{self.title} {self.created_at} {self.status}'
