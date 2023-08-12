from django.contrib import admin
from projects.models import Projects

# Register your models here.
class projectsAdmin(admin.ModelAdmin):
    list_display = ('p_id', 'p_title', 'p_short', 'p_description', 'p_img')

admin.site.register(Projects,projectsAdmin)