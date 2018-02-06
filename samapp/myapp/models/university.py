from django.db import models
from .common import Common


class University(Common):
    name = models.CharField(max_length=50)

    owner = models.ForeignKey('auth.Group', related_name='universities', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "University"
        verbose_name_plural = "Universities"
        ordering = ['name']

    def __str__(self):
        return '%s:%s:%s' % (self.name, self.last_mod_date, self.id)

    def save(self, *args, **kwargs):
        # self.last_mod_date = datetime.now().date()
        super(University, self).save(*args, **kwargs)
