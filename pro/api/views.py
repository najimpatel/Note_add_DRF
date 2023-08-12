from django.shortcuts import render
# from rest_framework import generics

from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets 

# Create your views here.
class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer