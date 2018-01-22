import uuid
from django.db import models

from samapp.myapp.models import University


class Student(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return '%s:%s:%s' % (self.first_name, self.last_name, self.id)

