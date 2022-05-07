from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ['user', 'page_name', 'page_cat']
    
