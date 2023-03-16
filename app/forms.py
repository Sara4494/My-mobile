from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import Form, ModelForm, DateField, widgets
from app.models import *

class SpareForm(forms.ModelForm):
    class Meta:
        model = Spare
        fields = ['name']
        

class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class UpdateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['brand','imageDev','modeldev']

class CreateDeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = [
            'brand','nameDev','imageDev','networkDev',
            'announcedDev',
            'statusDev',
            'dimensionsDev',
            'wightDev',
            'buildDev',
            'simDev',
            'displayTypeDev',
            'displaySizeDev',
            'displayResDev',]
        #exclude = ['done']
        #widgets = {
            #'date_visit': widgets.DateInput(attrs={'type': 'date'}),
            #'content': widgets.SelectMultiple()
        #}
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model =  Profile
        fields = ['user','first_name','last_name','image']

class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model =  Profile  
        fields =['user','first_name','last_name','image']

class CreateAccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories
        fields =['name','details']

class UpdateAccessoriesForm(forms.ModelForm):
    class Meta:
        model = Accessories  
        fields =['name','details']
        
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields =['slug','name','logo']
        widgets ={
           'slug' :forms.TextInput(attrs={'class':'form-control'}),
           'name' :forms.TextInput(attrs={'class':'form-control'}),
           'logo' :forms.FileInput(attrs={'class':'form-control'}),
        }
        

class CreateServiceForm(forms.ModelForm):
    class Meta:
        model = Service  
        fields =['name','type','created_by','fixed_by','mobile','fixed_at']
        

class CreateBrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['slug','name','logo']
        
class CreateSpareForm(forms.ModelForm):
    class Meta:
        model = Spare
        fields = [
            'name',
            'fault',
            'name_to_cstmr',
            'device',
            'quality',
            'quality_degree',
            'cost',
            'brand_dev',
            'delivery',
            'price',
            'stotre',
            'price_in_trade_in_offer',
            'slug',
        ]
        
class CreateStoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = [
            'name',
            'location',
            'engineer_name',
            'category',
            'brands',
            'created_at',
            'slug',
        ]
        
        
        
        
        
        
class FixSpareForm(forms.ModelForm):
    class Meta:
        model = Spare
        fields = [
        'name',
        'fault',
        'name_to_cstmr',
        'device',
        'quality',
        'quality_degree',
        'cost',
        'brand_dev',
        'delivery',
        'price',
        'stotre',
        'price_in_trade_in_offer',
        'slug',
        ]
        
        
 