from django.shortcuts import render
from django.http import HttpResponse
from .models import Room 
# Create your views here.
'''
Views take HTTP requests and returns HTTP responses. Views are usually
put in a file called views.py located in each app's respective folder 
'''

# variable that keeps track of the rooms that we have 
# rooms = [
#     {"id": 1, 'name': "Let's learn python!"},
#     {"id": 2, 'name': "Design with me "}, 
#     {"id": 3, 'name': "Frontend stuff"},
    
# ]

# home route 
def home(request):
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

# room route 
def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {}
    context["room"] = room

    return render(request, 'base/room.html', context)