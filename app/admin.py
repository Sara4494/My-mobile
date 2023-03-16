from django.contrib import admin
from app.models import *

from import_export.admin import ImportExportModelAdmin

class ModelImportExport(ImportExportModelAdmin):
    pass

class DeviceAdmin(admin.ModelAdmin):
    #list_display_links = ['brand']
    list_display = ['nameDev',
                    'brand',
                    'slug_dev',
                    'imageDev',
                    ]
    list_editable = ['slug_dev','imageDev']
    list_per_page = 100
    list_filter = ['brand']

class BrandAdmin(admin.ModelAdmin):
    list_display = ['name','slug','get_devices_count']
    list_editable = ['slug']
    
class StoreAdmin(admin.ModelAdmin):
  
    list_display = ['name','location','engineer_name','category','brands','created_at']
    search_fields = ['brands']
    list_filter = ['name','location','engineer_name','category','brands','created_at']
    

# Register your models here.
admin.site.register(User)
admin.site.register(Brand,BrandAdmin)
admin.site.register(Device,DeviceAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(Spare)
admin.site.register(Profile)
admin.site.register(Product)
admin.site.register(Shop)
admin.site.register(Accessories)
admin.site.register(Service)
