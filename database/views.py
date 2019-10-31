from django.shortcuts import render
from django.http import HttpResponse
from .models import apt_building

# Create your views here.
def dashboard(request):
    apt_buildings = apt_building.all_buildings()
    return render(request, "database/dashboard.html", {"apt_buildings": apt_buildings } )

def building_toolbox(request, building_ID):
    building = apt_building.get_building(pk=building_ID)
    return  render(request, "database/toolbox_building.html", {"building": building})


 