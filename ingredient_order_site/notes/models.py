from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Note(models.Model):
    title = models.CharField(max_length=32)
    body = models.TextField()
    creation_datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['creation_datetime']


class NoteItem(models.Model):
    note = models.ForeignKey('Note', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def __str__(self):
        return self.note

    class Meta:
        ordering = ['-note']