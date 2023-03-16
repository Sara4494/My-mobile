from django.db import models
from app.choices import *
#from app.brand.model import Brand
from django.utils.text import slugify

class Device(models.Model):
    slug_dev = models.SlugField(("Slug"),blank=True,null=True)
    brand = models.ForeignKey("app.Brand", blank=True, null=True, on_delete=models.PROTECT)
    modeldev = models.CharField(max_length=20, blank=True, null=True)
    nameDev = models.CharField( max_length=120, verbose_name=("Name"))
    networkDev = models.CharField(max_length=200, blank=True, null=True, verbose_name=("Network"))
    announcedDev = models.CharField(max_length=200, blank=True, null=True, verbose_name=("Announced"))
    statusDev = models.CharField(max_length=200, blank=True, null=True, verbose_name=("Status"))
    dimensionsDev = models.CharField(max_length=200, verbose_name=("Device Dimensions"), blank=True, null=True)
    wightDev = models.CharField(max_length=200, verbose_name=("Device Wight"), blank=True, null=True)
    buildDev = models.CharField(max_length=200, verbose_name=("Build"), blank=True, null=True)
    simDev = models.CharField(max_length=200, verbose_name=("Sim"), blank=True, null=True)
    displayTypeDev = models.CharField(max_length=200, verbose_name=("Screen Type"), blank=True, null=True)
    displaySizeDev = models.CharField(max_length=200, verbose_name=("Screen Size"), blank=True, null=True)
    displayResDev = models.CharField(max_length=200, verbose_name=("Screen Resolution"), blank=True, null=True)
    oSDev = models.CharField(max_length=150, verbose_name=("Android"), blank=True, null=True)
    chipsetDev = models.CharField(max_length=150, verbose_name=("Chipset"), blank=True, null=True)
    cPUDev = models.CharField(max_length=300, verbose_name=("CPU"), blank=True, null=True)
    cardSlotDev = models.CharField(max_length=50, verbose_name=("Card Slot"), blank=True, null=True)
    internalDev = models.CharField(max_length=200, verbose_name=("Device Storage"), blank=True, null=True)
    mainCameraDev = models.CharField(max_length=300, verbose_name=("Main Camera"), blank=True, null=True)
    main_camera_featuresDev = models.CharField(max_length=150, verbose_name=("Features Main Camera"), blank=True, null=True)
    main_camera_videoDev = models.CharField(max_length=150, verbose_name=("Main Camera Video"), blank=True, null=True)
    selfieCameraDev = models.CharField(max_length=200, verbose_name=("Selfie Camera"), blank=True, null=True)
    selfie_camera_videoDev = models.CharField(max_length=100, verbose_name=("Selfie Camera Video"), blank=True, null=True)
    loudspeakerDev = models.CharField(max_length=100, verbose_name=("Loudspeaker"), blank=True, null=True)
    wlanDev = models.CharField(max_length=100, verbose_name=("WLAN"), blank=True, null=True) 
    bluetoothDev = models.CharField(max_length=100, verbose_name=("Bluetooth"), blank=True, null=True)
    nfcDev = models.CharField(max_length=100, verbose_name=("NFC"), blank=True, null=True)
    radioDev = models.CharField(max_length=100, verbose_name=("Radio"), blank=True, null=True)
    usbDev = models.CharField(max_length=100, verbose_name=("USB"), blank=True, null=True)
    sensorsDev = models.CharField(max_length=100, verbose_name=("Sensors"), blank=True, null=True)
    batteryDev = models.CharField(max_length=100, verbose_name=("Battery Type"), blank=True, null=True)
    PriceDev = models.CharField(max_length=100, verbose_name=("Price"), blank=True, null=True)
    imageDev = models.ImageField(upload_to='Devices/Devices_Img/', verbose_name=("Image Device"), blank=True)
    img_dev_full_1 = models.ImageField(upload_to='Devices/Devices_full_pic/', verbose_name=("Full Image 1 (or front)"), blank=True)
    img_dev_full_2 = models.ImageField(upload_to='Devices/Devices_full_pic/', verbose_name=("Full Image 2 (or back)"), blank=True)
    def save(self,*args,**kwargs):
        if not self.slug_dev:
            self.slug_dev = slugify(self.nameDev)
        super(Device,self).save(*args,**kwargs)
    
    def __str__(self):
        return self.nameDev