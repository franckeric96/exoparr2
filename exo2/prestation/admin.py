from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

class SuiteAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','nom']}),
        ('Status',{'fields': ['prix','status']})
       
    ]
    
    list_display = ('nom','date_add','prix','status','image_views')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

                                                                                                                                  
    
class ServiceAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','nom']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('nom','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

   


    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Service, ServiceAdmin)  
_register(models.Suite, SuiteAdmin)
