from django.forms import ModelForm

from bookshelfapp.models import Bookshelf


class WriteForm(ModelForm):
    class Meta:
        model = Bookshelf
        fields = ['review','transcription']
