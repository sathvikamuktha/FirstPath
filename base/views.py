from django.shortcuts import render
# from django.http import HttpResponse

rooms = [
    {'id':1, 'name' : 'Job Posting page!'},
    {'id':2, 'name' : 'Profile settings '},
    {'id':3, 'name' : 'Feature 1'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room' : room}
    return render(request, 'base/room.html', context)
