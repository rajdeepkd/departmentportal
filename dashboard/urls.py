from django.urls import path
from . import views
from dashboard.views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('notes', views.notes, name="notes"),
    path('delete_notes/<int:pk>', views.delete_note, name="delete-notes"),
    path('notes_detail/<int:pk>', views.NotesDetailView.as_view() , name="notes-detail"),
]
