from django.db import models
from app.choices import *
from app.models import Device
from django.utils.text import slugify

class Brand(models.Model):
    # logo
    slug = models.SlugField(("Slug"),blank=True,null=True)
    name = models.CharField( choices=brand_name , max_length=100 , verbose_name=('اسم البراند'))
    logo = models.ImageField(upload_to='brandslogo', verbose_name=("Logo Brand"),null=True , blank=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Brand,self).save(*args,**kwargs)
    
    
    def __str__(self):
        return self.name
    
    def get_devices_count(self):
        return Device.objects.filter(brand=self).count()
    
    def get_devices(self):
        return Device.objects.filter(brand=self)
    