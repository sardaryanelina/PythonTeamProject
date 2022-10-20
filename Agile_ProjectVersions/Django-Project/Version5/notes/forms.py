
from django.core.exceptions import ValidationError
from django import forms

from .models import Note

class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-5'}),
            'text': forms.Textarea(attrs={"class": "form-control mb-5"})
        }
        labels = {
            'text': "Write your post here:"
        }

# Example of title validation function
    #def clean_title(self):
    #    title = self.cleaned_data['title'] #cleaned_data is a dictionary returned by form
    #    if 'Django' not in title:
    #        raise ValidationError('We only accept notes about Django!')
    #    return title