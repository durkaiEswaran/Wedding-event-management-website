from django.contrib import admin
from .models import Venue,Catering,BookingVenue,BookingCatering,Photography,BookingPhotography,StageDecoration,BookingStageDecor,Contact,WeddingPackage
class VenuAdmin(admin.ModelAdmin):
    list_display = ('name','location','availability')

# Register your models here.
admin.site.register(Venue,VenuAdmin)
admin.site.register(BookingVenue)
admin.site.register(Catering)
admin.site.register(BookingCatering)
admin.site.register(Contact)
admin.site.register(StageDecoration)
admin.site.register(BookingStageDecor)
admin.site.register(Photography)
admin.site.register(BookingPhotography)
admin.site.register(WeddingPackage)

