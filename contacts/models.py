from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    job_position = models.CharField(max_length=30, null=True)
    
    def __str__(self) -> str:
        return f'{self.id} {self.first_name} {self.last_name} {self.email} {self.job_position}'