from django.contrib import admin
from .models import tool, toolbox, apt_building, bike_company, bike_video

#class StepInline(admin.StackedInline):
    #model = toolbox

    
#class apt_buildingAdmin(admin.ModelAdmin):
    #inlines = [StepInline,]

# Register your models here.
admin.site.register(tool)
admin.site.register(toolbox)
admin.site.register(apt_building)
admin.site.register(bike_company)
admin.site.register(bike_video)
