from django.db import models

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
        toolbox = models.ForeignKey("toolbox", on_delete=models.CASCADE)
        video = models.ManyToManyField('bike_video')
class toolbox(models.Model): 
        RENT_STATUS = [('K', 'KEEP'), ('R', 'RETURNED')]
        toolbox_ID = models.CharField(max_length=50)
        time_update = models.DateTimeField(auto_now = True)
        description = models.TextField()
        amount = models.IntegerField()
        rent_status = models.CharField(choices=RENT_STATUS, max_length=1)
        #Relationship to other data
        building = models.ForeignKey("apt_building", on_delete=models.CASCADE)
        user_rent = models.ForeignKey('user',on_delete=models.CASCADE, blank=True)
        sponsor = models.ManyToManyField('bike_company', blank=True)
        
class apt_building(models.Model):
        address = models.CharField(max_length=50)
        time_update = models.DateTimeField(auto_now=True)
        description = models.TextField()
       

#nen tao rieng user
class user(models.Model):
        RENT_STATUS = [('K','KEEP'),('R','RETURNED'),]
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=50)
        email = models.CharField(max_length=50)
        subcription_date = models.DateTimeField()
        rent_status = models.CharField(choices=RENT_STATUS, max_length=1,)
        rent_date = models.DateTimeField()
        returen_date = models.DateTimeField
        description = models.TextField()
        #Relationship to other data
        building = models.ForeignKey(apt_building, on_delete=models.CASCADE)

class bike_company(models.Model):
        name = models.CharField(max_length=50)
        address = models.CharField(max_length=50)
        time_update = models.DateTimeField()
        description = models.TextField()

class bike_video(models.Model):
        name = models.CharField(max_length=50)
        category = models.CharField(max_length=50)
        time_create = models.DateTimeField(auto_now_add = True)
        tiem_update = models.DateTimeField(auto_now = True)
        description = models.TextField()
