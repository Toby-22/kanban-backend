from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact_profile', null=True, blank=True)
    job_position = models.CharField(max_length=30, null=True)
    
    def __str__(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.email} {self.job_position}'