
from django.shortcuts import render ,redirect ,get_object_or_404
from app.models import *
from app.forms import *
from app.filters import *
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')

def all_profile(request):
    all_profile =  Profile.objects.all()
    
    context = {
        'all_profile': all_profile,
    }
    return render(request,'profile/all_profile.html',context)
    
    
def profile_detail(request,slug):
    try:
        profile = get_object_or_404( Profile,slug=slug)
        print(profile)
    except:
        profile = None
    context = {
         "profile":profile,
        }
    return render(request,'profile/profile_detail.html',context)

def create_profile(request):
    form = CreateProfileForm()
    if request.method == "POST":
        form = CreateProfileForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            #files = request.FILES.getlist('file_field')
            form.save()
            return redirect('all_profile')
        else:
            form = CreateProfileForm()
    context = {
        "title":"جهاز جديد",
        'form':form,
    }
    return render(request,'profile/create_profile.html',context)

def profile_update(request,slug):
    try:
        profile = get_object_or_404(Profile,slug=slug)
        print(profile)
    except:
        profile = None
    form = UpdateProfileForm(instance=profile)
    if request.method == "POST":
        print("POSTTTTTTTTTTTTTTTT")
        form = UpdateProfileForm(request.POST , request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('all_profile')
        else:
            form = CreateProfileForm(instance=profile)
    context = {
        'title':"تعديل فى الجهاز",
        'form':form,
        }
    return render(request,'profile/profile_update.html',context)
 