from django.urls import path
from app.views import *

urlpatterns = [
    path('',home,name='home'),
    
    ## 127.0.0.1:8000/app/home/
    ### Mobile
    path('all_devices',all_devices,name='all_devices'),
    path('device/<slug:slug>/',device_detail,name='device_detail'),
    path('create_device',create_device,name='create_device'),
    path('device_update/<slug:slug>/',update_device,name='device_update'),
    path('delete/<int:id>/',delete, name="delete"),
    
    # delete
    
    ### Brand
    path('all_brands',all_brands,name='all_brands'),
    path('brand/<slug:slug>/',brand_details,name='brand_details'),
    path('update/<slug:slug>/',update,name='update'),
    path('create_brand',create_brand,name='create_brand'),
    
    # create
    # update
    # delete
    
    ### Store
    path('all_stores',all_stores,name='all_stores'),
    path('store_detail/<slug:slug>/',store_detail,name='store_detail'),
    path('create_store',create_store,name='create_store'),
    # update
    # delete
    
    ### Profile
    path('all_profile',all_profile,name='all_profile'),
    path('profile_detail/<slug:slug>/',profile_detail,name='profile_detail'), 
    path('create_profile',create_profile,name='create_profile'),
    path('profile_update/<slug:slug>/',profile_update,name='profile_update'),
    # delete
    
    ### Spare
    path('all_spare',all_spare,name='all_spare'),
    path('spare_detail/<slug:slug>/',spare_detail,name='spare_detail'),
    path('create_spare',create_spare,name='create_spare'),
    # update
    # delete
    
    ### Accessories
    path('all_ccessories',all_ccessories,name='all_ccessories'), # all
    path('accessories_detail/<slug:slug>/',accessories_detail,name='accessories_detail'), # detail
    path('accessories_create',accessories_create,name='accessories_create'),# create
    path('accessories_update/<slug:slug>/',accessories_update,name='accessories_update'), # update
    # delete
    
    ### Service
    path('all_fix',all_fix,name='all_fix'),
    path('fix_device',fix_device,name='fix_device'),
    path('fix_update/<slug:slyg>/',fix_update, name="fix_update"),
 
    path('fix_delete/<int:id>/',fix_delete, name="fix_delete"),
    
    # all
    # detail
    # create > 
    # update
    # delete
    
    ### Product
    # all
    # detail
    # create > create or get for FK
    # update
    # delete
    
    ## User
    path('register_customer',register_customer,name='register_customer'),
    path('register_tager',register_tager,name='register_tager'),
    
    ### Url 3ama l aktr mn 7aga f el project
    path('form_bootstrap',form_bootstrap,name='form_bootstrap'),
 
]