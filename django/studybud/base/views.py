from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
'''
Views take HTTP requests and returns HTTP responses. Views are usually
put in a file called views.py located in each app's respective folder 
'''

# home route 
def home(request):
    return render(request, 'home.html')

# room route 
def room(request):
    return render(request, 'room.html')