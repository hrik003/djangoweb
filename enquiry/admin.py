from django.contrib import admin
from enquiry.models import Enquiry
# Register your models here.
class enquiryAdmin(admin.ModelAdmin):
    list_display= ('fname','lname','email','phone','message')

admin.site.register(Enquiry,enquiryAdmin)