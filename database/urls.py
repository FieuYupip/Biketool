from django.urls import path
from . import views
urlpatterns = [
    path('', views.dashboard, name ='dashboard'),
    path('<int:building_ID>', views.building_toolbox, name ='building_toolbox'),
    
]
