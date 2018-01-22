import uuid
from django.db import models


class University(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    last_mod_date = models.DateField()

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        ordering = ['name']

    def __str__(self):
        return '%s:%s:%s' % (self.name, self.last_mod_date, self.id)

