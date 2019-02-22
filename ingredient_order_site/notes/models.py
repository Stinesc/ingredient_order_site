from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Note(models.Model):
    title = models.CharField(verbose_name=_('Title'), max_length=32)
    body = models.TextField(verbose_name=_('Body'))
    creation_datetime = models.DateTimeField(verbose_name=_('Creation datetime'), auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return _(self.title)

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
