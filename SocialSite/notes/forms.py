from turtle import title
from django import forms
from .models import Notes
from django.core.exceptions import ValidationError

class Notesform(forms.ModelForm):
    class Meta:
        model= Notes
        fields=('title','text')
        labels={
        'text': 'what would you like to note?'
    }

def clean_title(self):
    title= self.cleaned_data['title']
    if 'Django' not in title:
        raise ValidationError("Needs django")
    return title