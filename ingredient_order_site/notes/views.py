from django.views.generic import FormView, ListView, TemplateView


class NotesTemplateView(TemplateView):
    template_name = "notes/notes_type_selection.html"
