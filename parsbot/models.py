from django.db import models


class BaseCreateUpdateModel(models.Model):
    create_at = models.DateTimeField(auto_created=True)
    modified_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
