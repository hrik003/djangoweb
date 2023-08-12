from django.contrib import admin
from sociallink.models import SocialLink

# Register your models here.
class socialLinkAdmin(admin.ModelAdmin):
    list_display= ('sl_name','sl_url','sl_icon')

admin.site.register(SocialLink,socialLinkAdmin)