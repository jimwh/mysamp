import uuid
from django.db import models


class Common(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    last_mod_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True
