

from django.db import models
from app.choices import *
 
 
from django.utils.text import slugify

class Store(models.Model):
    name = models.CharField(max_length=200, choices=area_list, verbose_name=("اسم الفرع / المحل"), blank=True, null=True)
    location = models.CharField(max_length=200,choices=city_list, verbose_name=("المكان"), blank=True, null=True)
    engineer_name = models.CharField(max_length=200, choices = list_angineer,verbose_name=("اسم المهندس"), blank=True, null=True)
    category = models.CharField(max_length=200,choices= area_list, verbose_name=("النوع : التوكيل / المحل"), blank=True, null=True)
    brands = models.CharField(max_length=300, choices=brand_name, verbose_name=("اسم البراند"), blank=True, null=True)
    created_at = models.DateTimeField(blank=True,null=True)
    slug = models.SlugField(("Slug"),blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.brands)
        super(Store,self).save(*args,**kwargs)
      
    
    ## Date Time Field (created_at)
    ## Add City List To Store
    ## number of engineer = integerfield
    
    def __str__(self):
        #db_tables = "store"
        return str(self.name)