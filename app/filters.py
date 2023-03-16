import django_filters
from app.models import *

class DeviceFilter(django_filters.FilterSet):
    class Meta:
        model = Device
        #fields = ['nameDev', 'brand']
        fields = {
            ### icontains
            ### contains
            ### iexact
            ### exact
            'nameDev': ['icontains'],
            'brand':['exact'],
        }

class StoreFilter(django_filters.FilterSet):
    class Meta:
        model = Store
        fields = {
            'name': ['icontains'],
        }
class SpareFilter(django_filters.FilterSet):
    class Meta:
        model = Spare
        fields = {
            'name': ['icontains'],
        }
   