from django.forms import ModelForm
from reviewapp.models import Review


class WriteForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review','transcription']
