from django.contrib import admin

from . import models
# Register your models here.
admin.site.register(models.Suite)
admin.site.register(models.Service)
