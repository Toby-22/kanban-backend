from django.db import models
from django.conf import settings
import datetime

class Todos(models.Model):
    STATUS = [
        ('todo', 'todo'),
        ('inWork', 'inWork'),
        ('inReview', 'inReview'),
        ('done', 'done'),
    ]      
        
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    created_at = models.DateField(default=datetime.date.today)
    due_date = models.DateField()
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, default='todo', max_length=30)
    category = models.CharField(max_length=30)
    
    def __str__(self):
        return f'{self.id} {self.title} {self.created_at} {self.status}'
    

