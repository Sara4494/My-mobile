from django.db import models
from .choices import *
from django.utils.text import slugify
from app.device.model import *
from app.brand.model import *
from app.profile.models import *
from app.store.models import *

# Create your models here.

class Spare(models.Model):
    # قطع الغيار للعملاء 
    name = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("اسم القطعة"))
    fault = models.CharField(max_length=50, verbose_name=(" العطل الناتج عن تلف القطعة"), choices=fault_tocustomer, blank=True, null=True,)
    name_to_cstmr = models.CharField(max_length=50, verbose_name=("نوع القطعة"), choices=spareparts, blank=True, null=True,)
    device = models.ForeignKey(Device ,verbose_name=("اسم الجهاز"), blank=True, null=True, on_delete=models.PROTECT)
    quality = models.CharField(max_length=200 , choices=quality_category, verbose_name=('جودة القطعة'), blank=True, null=True,)
    quality_degree = models.CharField(max_length=20, verbose_name=("درجة الجودة"),choices=quality_degree , blank=True, null=True,)
    cost = models.DecimalField(max_digits=6,verbose_name=("تكلفة القطعة"), decimal_places=2, blank=True, null=True)
    brand_dev = models.ForeignKey(Brand , related_name='Brandspr' , blank=True, null=True , verbose_name=("اسم البراند"), on_delete=models.PROTECT)
    delivery = models.CharField(max_length=100 , blank=True, null=True )
    price = models.IntegerField( verbose_name=("السعر"))
    stotre = models.ForeignKey(Store , blank=True, null=True, on_delete=models.PROTECT)
    price_in_trade_in_offer = models.CharField(max_length=200, blank=True, null=True)
    slug = models.SlugField(("Slug"),blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Spare,self).save(*args,**kwargs)

    def __str__(self):
         return self.name

class Service(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("اسم الخدمة"))
    type = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("نوع الخدمة"))
    created_by = models.ForeignKey(Profile , related_name="created_by", on_delete=models.CASCADE , verbose_name="العميل (طالب الخدمة)")
    fixed_by = models.ForeignKey(Profile , related_name="fixed_by", on_delete=models.CASCADE, verbose_name="التاجر (مقدم الخدمة)")
    mobile = models.ForeignKey('app.Device',on_delete=models.CASCADE,null=True,blank=True )
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    fixed_at = models.DateTimeField(null=True,blank=True)
    def __str__(self):
         return self.name

class Accessories(models.Model):
   name = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("اسم الاكسسوار"))
   image = models.ImageField(verbose_name=("Devices/Devices_Img/"),upload_to='image',blank=True, null=True)
   details = models.CharField(max_length=200, blank=True, null=True ,verbose_name=("التفاصيل"))
   color =  models.CharField(max_length=10, blank=True, null=True ,verbose_name=("الون"))
   trade_mark =models.CharField(max_length=10, blank=True,null=True,verbose_name=("العلامة التجارية") )
   price = models.IntegerField( verbose_name=("السعر"))
   slug = models.SlugField(("Slug"),blank=True,null=True)
   def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Accessories,self).save(*args,**kwargs)
    
   def __str__(self):
         return self.name
class Shop(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("الاسم"))
    outlet = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("منفذ البيع - "))
    the_address = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("العنوان "))
    region = models.CharField(max_length=50, blank=True, null=True ,verbose_name=("المنطقة "))
    def __str__(self):
         return self.name

class Product(models.Model):
    device = models.ForeignKey("app.Device", blank=True, null=True, on_delete=models.PROTECT)
    accessories = models.ForeignKey( Accessories, blank=True, null=True, on_delete=models.PROTECT)
    spare = models.ForeignKey( Spare, blank=True, null=True, on_delete=models.PROTECT)
    price = models.IntegerField( verbose_name=("السعر"))
    def __str__(self):
         return self.device
