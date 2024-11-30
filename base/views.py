from django.shortcuts import render
# from django.http import HttpResponse
from .models import Room

# rooms = [
#     {'id':1, 'name' : 'Job Posting page!'},
#     {'id':2, 'name' : 'Profile settings '},
#     {'id':3, 'name' : 'Feature 1'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room' : room}
    return render(request, 'base/room.html', context)
