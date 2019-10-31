from django.db import models
from datetime import timedelta
import datetime


# Create your models here.
class tool(models.Model):
        QUALITY_STATUS = [('G', 'Good'),('B', 'Bad'),]
        name = models.CharField(max_length=50)
        category = models.CharField(max_length=50)
        time_update = models.DateTimeField(auto_now=True)
        description = models.TextField()
        amount = models.IntegerField(default=0)
        quality = models.CharField(choices=QUALITY_STATUS, max_length=1)
        #Relationship to other data
        toolbox = models.ForeignKey("toolbox", on_delete=models.CASCADE, null=True, blank=True )
        video = models.ManyToManyField('bike_video')
        def __str__(self):
                return self.name
        class meta:
             ordering =('name')   
class toolbox(models.Model): 
        RENT_STATUS = [('K', 'KEEP'), ('R', 'RETURNED')]
        toolbox_ID = models.CharField(max_length=50)
        time_add = models.DateTimeField(auto_now = True)
        description = models.TextField()
        rent_status = models.CharField(choices=RENT_STATUS, max_length=1)
        rent_date = models.DateField(null=True, blank=True)
        avaiable_date = models.DateField(null=True, blank=True)
        #Relationship to other data
        building = models.ForeignKey("apt_building", on_delete=models.CASCADE, null=True, blank=True)
        sponsor = models.ManyToManyField('bike_company')
        def __str__(self):
                return 'Toolbox ID %s, Adress %s, Rent_status %s' % (self.toolbox_ID, self.building, self.rent_status)
        class meta:
                ordering =('name')  
        def save(self, *args, **kwargs):
                delta= timedelta(days=5)
                if self.rent_status == 'KEEP':
                        self.avaiable_date =  self.rent_date + delta
                else:
                        self.avaiable_date = datetime.datetime.now()
                super(toolbox, self).save(*args, **kwargs)
      
        
        
                
        
class apt_building(models.Model):
        address = models.CharField(max_length=50)
        time_update = models.DateTimeField(auto_now=True)
        description = models.TextField()
        def all_buildings():
                return apt_building.objects.all()
        
        def get_building(pk):
                return apt_building.objects.get(pk = pk)


        def __str__(self):
                return self.address
        class meta:
                ordering = ('address',)

#nen tao rieng user


class bike_company(models.Model):
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=50)
        time_update = models.DateTimeField()
        description = models.TextField()
        def __str__(self):
                return self.name
        class meta:
                ordering = ('name')

class bike_video(models.Model):
        name = models.CharField(max_length=50)
        category = models.CharField(max_length=50)
        time_create = models.DateTimeField(auto_now_add = True)
        tiem_update = models.DateTimeField(auto_now = True)
        description = models.TextField()
        def __str__(self):
                return self.name
        class meta:
                ordering = ('name')

