import uuid
from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255)
    featured_image = models.ImageField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
