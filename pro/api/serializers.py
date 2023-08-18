from .models import Note

class Noteserializer(serializers.Modelserializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'text')
