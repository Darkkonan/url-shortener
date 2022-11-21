from django.db import models
import uuid


class Link(models.Model):
    manage = True
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    link = models.CharField(max_length=255)
