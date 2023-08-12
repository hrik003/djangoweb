from django.contrib import admin
from webservice.models import WebService

# Register your models here.
class webServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id','service_img', 'service_title', 'service_sub')

admin.site.register(WebService,webServiceAdmin)