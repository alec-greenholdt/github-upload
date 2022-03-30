from msilib.schema import ListView
from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView
# Create your views here.

from .models import Notes

class NotesListView(ListView):
    model= Notes
    context_object_name= 'notes'
    template_name='templates/notes/notesList.html'

#above is class versioon of it
# def list(request):
#     allNotes=Notes.objects.all()
#     return render(request, 'templates/notes/notesList.html',{'notes': allNotes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name='note'
    template_name= 'templates/notes/getnote.html'
    
# def detail(request,pk):
#     try:
#         note= Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("ya didnt do it right")
#     return render(request, 'templates/notes/getnote.html',{'note': note})
