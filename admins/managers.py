from django.db import models

class PublishedAdminManager(models.Manager):
    def get_queryset(self) -> models.QuerySet:
        return super().get_queryset().filter(is_published=True)
