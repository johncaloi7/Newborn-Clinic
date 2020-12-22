from django.contrib import admin
from .models import Detail

# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'header')
    list_display_links = ('id', 'header')

admin.site.register(Detail, DetailAdmin)    