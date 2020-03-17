from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe



# Register your models here.
class SocialAccountAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Presentation',{'fields': ['nom']}),
        ('reseaux', {'fields': ['icon','lien','status']})
        
    ]
    
    
    list_display = ('nom','date_add','status')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    
class InfoSiteAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Status',{'fields': ['site_map','status']})
       
    ]
    
    list_display = ('titre','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))


class GallerieAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('titre','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))


class TemoignageAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','nom','prenom']}),
        ('Status',{'fields': ['message','status']})
       
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

                                                                                                                                  
    
class PresentationAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','nom']}),
        ('Status',{'fields': ['description','status']})
       
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

_register(models.SocialAccount, SocialAccountAdmin)  
_register(models.Temoignage, TemoignageAdmin) 
_register(models.Gallerie, GallerieAdmin) 
_register(models.Presentation, PresentationAdmin) 
_register(models.InfoSite, InfoSiteAdmin) 


 