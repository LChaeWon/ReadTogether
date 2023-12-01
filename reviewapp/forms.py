from django.forms import ModelForm
from django_bootstrap5 import forms

from reviewapp.models import Review


class WriteForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review','transcription']
        labels = {
            "review": "감상평",
            "transcription": "필사",
        }
