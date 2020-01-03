from django.db import models


class BaseModelMixin(models.Model):
    class Meta:
        abstract=True

    is_active = models.BooleanField(default=True)
    created = models.DateTimeField('作成日時', auto_now_add=True)
    updated = models.DateTimeField('更新日時', auto_now=True)

    