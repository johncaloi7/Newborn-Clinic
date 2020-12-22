from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_title','is_featured', 'created_date')
    list_display_links = ('id', 'service_title')
    list_editable = ('is_featured',)

admin.site.register(Service, ServiceAdmin)    