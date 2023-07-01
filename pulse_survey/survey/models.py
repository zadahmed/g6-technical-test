import uuid

from django.db import models


class UUIDPrimaryKeyBase(models.Model):
    class Meta:
        abstract = True

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(editable=False, auto_now_add=True)
    modified_at = models.DateTimeField(editable=False, auto_now=True)

    class Meta:
        abstract = True


class Result(UUIDPrimaryKeyBase, TimeStampedModel):
    data = models.JSONField(null=True)
    session_id = models.UUIDField(default=uuid.uuid4, editable=False)
    page_number = models.IntegerField()


class Feedback(UUIDPrimaryKeyBase, TimeStampedModel):
    content = models.CharField(max_length=4096, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super().save(*args, **kwargs)
