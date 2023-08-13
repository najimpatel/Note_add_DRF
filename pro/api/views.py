from django.shortcuts import render
from .models import Note
from .serializers import NoteSerializer
from rest_framework import viewsets 


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
