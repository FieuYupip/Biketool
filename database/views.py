from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    name_of_service = "biketool rental service"
    return render(request, "database/home.html", {'name': name_of_service} )


 