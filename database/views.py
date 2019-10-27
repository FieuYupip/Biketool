from django.shortcuts import render
from django.http import HttpResponse
from .models import apt_building

# Create your views here.
def index(request):
    apt_buildings = apt_building.all_buildings()
    building = apt_building.building(1) 
    return render(request, "database/home.html", {"apt_buildings": apt_buildings } )


 