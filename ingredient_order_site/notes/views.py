from django.views.generic import FormView, ListView, TemplateView
from django.contrib.contenttypes.models import ContentType
from django.apps import apps
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import NoteForm
from .models import NoteItem


class NotesTemplateView(TemplateView):
    template_name = "notes/notes_type_selection.html"


class NoteCreateView(LoginRequiredMixin, FormView):
    template_name = 'notes/note_form.html'
    form_class = NoteForm

    def post(self, request, *args, **kwargs):
        obj_pk = kwargs.get('pk')
        obj_type = kwargs.get('type')
        model = apps.get_model('foodprod', obj_type)
        cont_obj = model.objects.get(pk=obj_pk)
        form = self.form_class(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            NoteItem.objects.create(content_object=cont_obj, note=note)
            return redirect('notes:notes')
        else:
            return self.form_invalid(form)


class NotesListView(ListView):
    model = NoteItem
    template_name = 'notes/notes.html'

    def get_queryset(self):
        model_type = self.kwargs['type']
        content = ContentType.objects.get(model=model_type)
        return self.model.objects.filter(content_type=content.id)
