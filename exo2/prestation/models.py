from django.db import models

# Create your models here.
class Suite(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Suite')
    prix = models.IntegerField
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Suite'
        verbose_name_plural = 'Suites'

    def __str__(self):
        return self.nom
    
    
class Service(models.Model):
    nom = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/Service')
    date_add = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=True)

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.nom