from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.SocialAccount)
admin.site.register(models.InfoSite)
admin.site.register(models.Gallerie)
admin.site.register(models.Temoignage)
admin.site.register(models.Presentation)

