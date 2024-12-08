from django.forms import ModelForm
from .models import Room, Project
from django import forms

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # ['name', 'body']
        exclude = ['host', 'participants']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']

from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'time', 'major']
