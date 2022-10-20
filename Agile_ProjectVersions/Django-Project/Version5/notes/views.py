from django.shortcuts import render
from django.http import Http404
from django.http.response import HttpResponseRedirect
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import NoteForm
from .models import Note
#This is how we display the notes we have created.

class NoteCreateView(CreateView):
    model = Note
    success_url = '/notes'
    form_class = NoteForm

    def form_valid(self, form):
        self.object = form.save(commit=False) #Creates the object, but doesn't save it to DB. Allows us to add user, then save.
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

class NoteUpdateView(UpdateView):
    model = Note
    success_url = '/notes'
    form_class = NoteForm

class NoteDeleteView(DeleteView):
    model = Note
    success_url = '/notes'
    template_name = 'notes/note_delete.html'

class NoteListView(LoginRequiredMixin, ListView):
    model = Note
    context_object_name = "notes" # default is "objects", but we changed it to "notes"
    template_name = "notes/note_list.html"
    login_url = "/login" # They will be redirected here. 

    def get_queryset(self):
        return self.request.user.notes.all()

# The ListView makes the query for us. 
# We also don't need to define a template name, 
# because we created a template name that follows the standard of that class-based view.
# However, if we were to change the template name, it might not work. So, we pass template_name to be safe.

# We replaced this function with the class-based view above.
#def list(request):
#    all_notes = Note.objects.all()
#    return render(request, 'notes/note_list.html', {'notes': all_notes})


class NoteDetailView(DetailView):
    model = Note
    context_object_name = "note" 
    template_name = "notes/note_details.html"

# No need for try/except, the class-based view takes care of the exception for us. 

# Sends all notes to the template. When the template is rendered, they will all be available. 

#def details(request, pk):
#    try:
#        note = Note.objects.get(pk=pk)
#    except Note.DoesNotExist:
#        raise Http404("Note does not exist.")
#    return render(request, 'notes/note_details.html', {'note': note})