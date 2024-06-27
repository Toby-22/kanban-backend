""" contac class """
from django.contrib.auth.models import User
from django.db import models


class Contact(models.Model):
    """ contact model """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contact_profile',
                                null=True, blank=True)
    job_position = models.CharField(max_length=30, null=True)
    def __str__(self) -> str:
        """ return the job position of a contact """
        return f'{self.job_position}'
