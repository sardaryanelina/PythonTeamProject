import imp
from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView


from .models import Note

class NoteListView(ListView):
    model = Note
    context_object_name = "notes" # default is "objects", but we changed it to "note"
    template_name = "note/notes_list.html"

class NoteDetailView(DetailView):
    model = Note
    context_object_name = "notes" 
    template_name = "note/notes_detail.html"


def detail(request, pk):
    try:
        note = Note.objects.get(pk = pk)
    except Note.DoesNotExist:
        raise Http404("Note does not exist.")
    return render(request, 'note/notes_detail.html', {'note': note})