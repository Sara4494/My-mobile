from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.decorators import login_required

from app.models import *

from app.forms import *
from app.filters import *
@login_required(login_url='login')

def all_devices(request):
    all_devices = Device.objects.all()
    device_filter = DeviceFilter()
    nameDev = None
    if 'search_name' in request.GET:
        nameDev = request.GET['search_name']
        if nameDev:
            all_devices = all_devices.filter(nameDev__icontains = nameDev)
   
          #  device_filter = DeviceFilter(request.GET)
          #  all_devices = DeviceFilter(request.GET).qs ## Query_set
 #   else:
        #device_filter = DeviceFilter()
    ## Query_set
    print('device')
    context = {
        "title":"All Devices Device",
        'all_devices':all_devices,
        'device_filter':device_filter,
        
    }
    return render(request,'device/all_devices.html',context)
    
def create_device(request):
    form = CreateDeviceForm()
    if request.method == "POST":
        form = CreateDeviceForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            #files = request.FILES.getlist('file_field')
            form.save()
            return redirect('all_devices')
        else:
            form = CreateDeviceForm()
    context = {
        "title":"جهاز جديد",
        'form':form,
    }
    return render(request,'device/create_device.html',context)
    
def update_device(request,slug):
    try:
        device = get_object_or_404(Device,slug_dev=slug)
        print(device)
    except:
        device = None
    form = UpdateDeviceForm(instance=device)
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTT")
        form = UpdateDeviceForm(request.POST , request.FILES,instance=device)
        if form.is_valid():
            form.save()
            return redirect('all_devices')
        else:
            form = CreateDeviceForm(instance=device)
    context = {
        'title':"تعديل فى الجهاز",
        'form':form,
        }
    return render(request,'device/device_update.html',context)
    
def device_detail(request,slug):
    try:
        device = get_object_or_404(Device,slug_dev=slug)
        print(device)
    except:
        device = None
    ## filter = list = loop
    ## get = object 1
    context = {
         "device":device,
        }
    return render(request,'device/device_details.html',context)
def delete (request,id):
    delete = get_object_or_404 (Device , id=id)
   
    if request.method == 'POST':
        delete.delete()
        return redirect('all_devices')
    return render(request,'device/delete.html')
    