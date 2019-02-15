from django.urls import path
from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.NotesTemplateView.as_view(), name='notes'),
    path('<str:type>/', views.NotesListView.as_view(), name='notes_by_type'),
    path('create/<str:type>/<int:pk>/', views.NoteCreateView.as_view(), name='note_create'),
]