from django.shortcuts import render ,redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from app.models import *
from app.forms import *

@login_required(login_url='login')
def all_brands(request):
    all_brand = Brand.objects.all()
    context = {
         "all_brand":all_brand,
        }
    return render(request,'brand/all_brands.html',context)

def create_brand(request):
    form = CreateBrandForm()
    if request.method == "POST":
        form = CreateBrandForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            #files = request.FILES.getlist('file_field')
            form.save()
            return redirect('all_brands')
        else:
            form = CreateBrandForm()
    context = {
        "title":"براند جديد",
        'form':form,
    }
    return render(request, 'brand/create_brand.html' ,context)

def brand_details(request,slug):
    brand = Device.objects.filter(brand__slug=slug)
    print("num devices")
    print(len(brand))
    context = {
         'brand':brand,
         "test":'test',
        }
    return render(request,'brand/brand_details.html',context)

def update(request,slug):
    try:
        brand = get_object_or_404(Brand , slug=slug)
        print(brand)
    except:
        brand = None
    form = BrandForm(instance=brand)
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTT")
        form = BrandForm(request.POST , request.FILES,instance=brand)
        if form.is_valid():
            form.save()
            return redirect('all_brands')
    context = {
        'title':"تعديل فى الجهاز",
        'form':form,
        }
    return render(request,'brand/brand_update.html',context)
    