from django.shortcuts import render , redirect ,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from app.forms import *
from app.models import *
from app.filters import *

from app.device.view import *
from app.brand.view import *
from app.profile.view import *
from app.store.view import *

cont = {}
## C Create > Request method = POST
## R  Read  > Request method = GET
## U Update > Request method = PUT
## D Delete > Request method = DELETE

def form_bootstrap(request):
    form_device = UpdateDeviceForm()
    form_spare = SpareForm()
    context = {
         "devs_all":Device.objects.all()[:5],
         "form_device":form_device,
         "form_spare":form_spare,
        }
    return render(request,'form_bootstrap.html',context)

def register_customer(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_customer = True
            instance.save()
            return redirect('login')
        else:
            form = RegisterUserForm(request.POST)
    cont['title'] = "التسجيل"
    cont['form'] = form
    return render(request,'registration/register_customer.html',cont)

def register_tager(request):
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.is_tager = True
            instance.save()
            return redirect('login')
        else:
            form = RegisterUserForm(request.POST)
    cont['title'] = "التسجيل"
    cont['form'] = form
    return render(request,'registration/register_tager.html',cont)

@login_required(login_url='login')
def home(request):
    #print(dir(request))
    print(request.path)
    #if request.user.is_autenticated:  
    #    if request.user.profile:
    #        profile = Service.objects.get(created_by=request.user)
            #services = Service.objects.filter(created_by=request.user)
    #        print(profile.first_name)
    #        print(request.user.profile.first_name)
    #else:
    #    return redirect("login")
    context = {
         #"services":services,
         "test":'test',
        }
    return render(request,'index.html',context)

        ##################
        ##### Brand ######
        ##################
      
        ##################
        ##### Device #####
        ##################
    
        ##################
        ##### Store ######
        ##################

 
        ##################
        ##### Spare ######
        ##################
        
@login_required(login_url='login')

def all_spare(request):
    all_spare =  Spare.objects.all()
    spare_filter = StoreFilter()
    if request.GET:
        spare_filter = StoreFilter(request.GET)
        all_spare = StoreFilter(request.GET).qs ## Query_set
    else:
         spare_filter = StoreFilter()
    
    context = {
        'all_spare': all_spare,
        'spare_filter':spare_filter
    }
    return render(request,'spare/all_spare.html',context)
    
def spare_detail(request,slug):
    try:
    
        spare = get_object_or_404( Spare,slug=slug)
        print(spare)
    except:
        spare = None
    
    context = {
         "spare":spare,
        }
    return render(request,'spare/spare_detail.html',context)
def create_spare(request):
    form = CreateSpareForm()
    if request.method == "POST":
        form = CreateSpareForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            #files = request.FILES.getlist('file_field')
            form.save()
            return redirect('all_spare')
        else:
            form = CreateSpareForm()
    context = {
        "title":"جهاز جديد",
        'form':form,
    }
    return render(request,'spare/create_spare.html',context)
    







        ##################
        ##### Profile ####
        ##################
@login_required(login_url='login')


def all_ccessories(request):
    all_ccessories =  Accessories.objects.all()
    context = {
        "title":"all_ccessories",
        'all_ccessories':all_ccessories,
        
    }
    return render(request,'accessories/all_ccessories.html',context)
    
def accessories_create(request):
    form = CreateAccessoriesForm()
    if request.method == "POST":
        form = CreateAccessoriesForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            #files = request.FILES.getlist('file_field')
            form.save()
            return redirect('all_ccessories')
        else:
            form = CreateAccessoriesForm()
    context = {
        "title":"جهاز جديد",
        'form':form,
    }
    return render(request,'accessories/accessories_create.html',context)
    
def accessories_update(request,slug):
    
    try:
        accessories = get_object_or_404(Accessories,slug=slug)
        print(accessories)
    except:
       accessories = None
    form = UpdateAccessoriesForm(instance=accessories)
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTT")
        form = UpdateAccessoriesForm(request.POST , request.FILES,instance=accessories)
        if form.is_valid():
            form.save()
            return redirect('all_ccessories')
        else:
            form = CreateAccessoriesForm(instance=accessories)
    context = {
        'title':"تعديل فى الجهاز",
        'form':form,
        }
    return render(request,'accessories/accessories_update.html',context)
    
def accessories_detail(request,slug):
    try:
        accessories = get_object_or_404(Accessories,slug=slug)
        print(accessories)
    except:
        accessories = None
    ## filter = list = loop
    ## get = object 1
    context = {
         "accessories":accessories,
        }
    return render(request,'accessories/accessories_detail.html',context)



 



   
from django.contrib.auth.decorators import login_required











 







def all_fix(request):
    all_fix = Spare.objects.all()
    context = {
         "all_fix":all_fix,
        }
    return render(request,'service/all_fix.html',context)





def fix_device(request):
  form = FixSpareForm()
  if request.method == "POST":
        form = FixSpareForm(request.POST,request.FILES)
        if form.is_valid():
            
            form.save()
       
        else:
            form = FixSpareForm()
  cont['title'] = 'اصلاح جهاز'
    #  cont['fix_device'] = fix_device
  cont['form'] = form
  cont['all_fix']= all_fix
  return render(request,'service/fix_device.html',cont)
 
 
 
def fix_update(request,slug):
    try:
        fix = get_object_or_404(Spare,slug=slug)
        print(fix)
    except:
        fix = None
    form = FixSpareForm(instance=fix)
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTT")
        form = FixSpareForm(request.POST , request.FILES,instance=fix)
        if form.is_valid():
            form.save()
            return redirect('all_devices')
        else:
            form = FixSpareForm(instance=fix)
    context = {
        'title':"تعديل",
        'form':form,
        }
    return render(request,'service/fix_update.html',context)
    
 
def fix_delete (request,id):
    delete = get_object_or_404 (Spare , id=id)
   
    if request.method == 'POST':
        delete.delete()
        return redirect('all_fix')
    return render(request,'service/fix_delete.html')
    