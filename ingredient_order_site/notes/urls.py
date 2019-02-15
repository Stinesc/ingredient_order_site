from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NotesTemplateView.as_view(), name='notes'),
    #path('<str:type>/', views.NoteListView.as_view(), name='notes_by_type'),
    #path('create/<str:type>/<int:pk>/', views.Note.as_view(), name='note_create'),
]