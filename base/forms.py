from django.forms import ModelForm
from .models import Room

from django import forms
from .models import Project
from .models import Room

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # ['name', 'body']
        exclude = ['host', 'participants']


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']
