from django.urls import path
from . import views

urlpatterns = [
   path('notes', views.NoteListView.as_view(), name="notes.list"), 
   path('notes/<int:pk>', views.NoteDetailView.as_view(), name="notes.detail"),
   path('notes/new', views.NoteCreateView.as_view(), name='notes.new'),
   path('notes/<int:pk>/update', views.NoteUpdateView.as_view(), name="notes.update"),
   path('notes/<int:pk>/delete', views.NoteDeleteView.as_view(), name="notes.delete"),
]

# 'notes' is the end of the url path
# views.list is the function to render the view we just created in views.py
# next step is to add this path in the main project urls.py folder
# second path will receive a value, pk, which is an integer
