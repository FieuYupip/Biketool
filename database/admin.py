from django.contrib import admin
from .models import tool, toolbox, apt_building, user, bike_company, bike_video

# Register your models here.
admin.site.register(tool)
admin.site.register(toolbox)
admin.site.register(apt_building)
admin.site.register(user)
admin.site.register(bike_company)
admin.site.register(bike_video)
