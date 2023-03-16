from django.db import models
from app.choices import *

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify

class User(AbstractUser):
    # username
    # password
    # email
    # first_name
    # last_name
    # is_staff
    # is_superuser
    # is_active
    is_customer = models.BooleanField(default=False)
    is_tager = models.BooleanField(default=False)

class Profile(models.Model):
    pos_site = (
        ('admin','Admin'),
        ('Customer','Customer'),
        ('Tager','Tager'),
        )
    ### لازم تفهمى انك تقدرى تدخلى على البروفايل من الريكوست اللى فيها ال user
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50 ,verbose_name="الاسم الاول", blank=True, null=True)
    last_name = models.CharField(max_length=50 ,verbose_name="اللقب", blank=True, null=True)
    phone_number = models.CharField(max_length=11,verbose_name="رقم التليفون",null=True , blank=True)
    phone_number2 = models.CharField(max_length=11,verbose_name="رقم التليفون 2",null=True , blank=True)
    addres = models.CharField(max_length=300 ,verbose_name="العنوان", blank=True, null=True)
    area = models.CharField(max_length=50 ,verbose_name="المنقطة", blank=True, null=True)
    mailo = models.EmailField(max_length=254,verbose_name="ايميل (بالشركة)", blank=True, null=True)
    image = models.ImageField(upload_to="Profiles/",verbose_name="صورة شخصية",blank=True, null=True)
    stores = models.ManyToManyField('app.Store',verbose_name="الفروع المسئول عنها",blank=True)    
    title = models.CharField(max_length=50 ,verbose_name="المسمى الوظيفى", blank=True, null=True)
    pos_in_store = models.CharField(max_length=50 ,choices=pos_site,verbose_name="صفته بالموقع", blank=True, null=True)
    slug = models.SlugField(("Slug"),blank=True,null=True)
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.user)
        super(Profile,self).save(*args,**kwargs)
    
    def __str__(self):
        return str(self.user)## Redius

@receiver(post_save,sender=User)
def create_profile_automatic(sender,instance,created,**kwargs):
    if created:
        if instance.is_customer:
            Profile.objects.create(
                user=instance,
                first_name=instance.first_name,
                last_name=instance.last_name,
                pos_in_store="Customer"
            )
        elif instance.is_tager:
            Profile.objects.create(
                user=instance,
                first_name=instance.first_name,
                last_name=instance.last_name,
                pos_in_store="Tager"
            )
        else:
            Profile.objects.create(
                user=instance,
                first_name=instance.first_name,
                last_name=instance.last_name,)