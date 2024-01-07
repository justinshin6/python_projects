from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
Views take HTTP requests and returns HTTP responses. Views are usually
put in a file called views.py located in each app's respective folder 
'''

# variable that keeps track of the rooms that we have 
rooms = [
    {"id": 1, 'name': "Let's learn python!"},
    {"id": 2, 'name': "Design with me "}, 
    {"id": 3, 'name': "Frontend stuff"},
    
]

# home route 
def home(request):
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

# room route 
def room(request, pk):
    context = {}
    for r in rooms:
        if r["id"] == int(pk):
            context["room"] = r

    return render(request, 'base/room.html', context)