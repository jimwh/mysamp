from django.db import models
from samapp.myapp.models import Common, University


class Student(Common):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    university = models.ForeignKey(University, on_delete=models.CASCADE)

    owner = models.ForeignKey('auth.Group', related_name='students', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        ordering = ['first_name', 'last_name']

    def __str__(self):
        return '%s:%s:%s' % (self.first_name, self.last_name, self.id)

