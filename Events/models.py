from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.
def getFileName(request,filename):
    now_time=datetime.now().strftime("%Y%m%d%H:%M:%S")
    new_filename = "%s%s"%(now_time,filename)
    return os.path.join('uploads/',new_filename)
    
class Venue(models.Model):
    name = models.CharField(max_length=80)
    image = models.ImageField(upload_to='venues/', null=True, blank=True)
    location = models.CharField(max_length=80)
    capacity = models.IntegerField()
    price_per_day = models.IntegerField()
    availability = models.BooleanField(default=True, help_text="1 - Available, 0 - Not Available")

    def __str__(self):
        return self.name 
    
class BookingVenue(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='bookings')
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.venue.name} on {self.booking_date} by {self.user_name}"
    
#creating model for catring services
class Catering(models.Model):
    Style = models.CharField(max_length=100,null=False,blank=False)
    image = models.ImageField(upload_to='catring/', null=True, blank=True)
    description = models.TextField(max_length=200,null=False,blank=False)
    pricePerGuest = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.Style
class BookingCatering(models.Model):
    catering = models.ForeignKey(Catering,on_delete=models.CASCADE,related_name='cateringbookings')
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    mobile_no = models.IntegerField()
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking for {self.catering.Style} on {self.booking_date} by {self.user_name}"

class StageDecoration(models.Model):
    style = models.CharField(max_length=80,blank=False,null=False)
    image = models.ImageField(upload_to="stagedecor/",null=True,blank=True)
    description = models.TextField(max_length=400,null=False,blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.style
class BookingStageDecor(models.Model):
    stageDecor = models.ForeignKey(StageDecoration,on_delete=models.CASCADE,related_name="stagedecoration")
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    mobile_no = models.IntegerField()
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking for {self.stageDecor.style} on {self.booking_date} by {self.user_name}"

class Photography(models.Model):
    type = models.CharField(max_length=80,blank=False,null=False)
    image = models.ImageField(upload_to='photography/',null=True,blank=True)
    description = models.TextField(max_length=400,null=False,blank=False)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    def __str__(self):
        return self.type
class BookingPhotography(models.Model):
    photography = models.ForeignKey(Photography,on_delete=models.CASCADE,related_name="photography")
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    mobile_no = models.IntegerField()
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking for {self.photography.type} on {self.booking_date} by {self.user_name}"

class WeddingPackage(models.Model):
    venue_img = models.ImageField(upload_to='wedding_package',null=False,blank=False)
    catering_img = models.ImageField(upload_to='wedding_package',null=False,blank=False)
    stage_img = models.ImageField(upload_to='wedding_package',null=False,blank=False)
    Photography_img = models.ImageField(upload_to='wedding_package',null=False,blank=False)
    name = models.CharField(max_length=50,null=False,blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    services = models.TextField(help_text="Enter services separated by commas,")

    def get_services_list(self):
        return self.services.split(',')

    def __str__(self):
        return self.name
    
class BookingPackage(models.Model):
    weddingpackage = models.ForeignKey(WeddingPackage,on_delete=models.CASCADE,related_name="weddingpackage")
    user_name = models.CharField(max_length=200)
    user_email = models.EmailField()
    mobile_no = models.IntegerField()
    additional_services = models.TextField(blank=True, help_text="Enter additional service requests.")
    booking_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Booking for {self.photography.type} on {self.booking_date} by {self.user_name}"
    
#contact page for getting feedback from the users

class Contact(models.Model):
    first_name = models.CharField(max_length=30,null=False,blank=False)
    last_name = models.CharField(max_length=30,null=False,blank=False)
    email = models.EmailField(null=False,blank=False)
    message = models.TextField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"feedback from {self.first_name}"



