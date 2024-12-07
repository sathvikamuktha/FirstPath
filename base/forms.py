from django.forms import ModelForm
from .models import Room

from .models import Room, Project

class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__' # ['name', 'body']
        exclude = ['host', 'participants']


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'link']
