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

def room(request):
    return render(request, 'room.html')
