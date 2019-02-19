from django.contrib import admin
from .models import NoteItem, Note


class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'creation_datetime', 'author')


class NoteItemAdmin(admin.ModelAdmin):
    list_display = ('content_type', 'object_id', 'content_object', 'note_title',
                    'note_body', 'note_creation_datetime', 'note_author')

    def note_title(self, obj):
        return obj.note.title

    def note_body(self, obj):
        return obj.note.body

    def note_creation_datetime(self, obj):
        return obj.note.creation_datetime

    def note_author(self, obj):
        return obj.note.author


admin.site.register(Note, NoteAdmin)
admin.site.register(NoteItem, NoteItemAdmin)
