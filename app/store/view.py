from django.shortcuts import render ,redirect ,get_object_or_404
from app.models import *
from app.forms import *
from app.filters import *


def all_stores(request):
    all_stores =  Store.objects.all()
    stores_filter = StoreFilter()
    if request.GET:
        stores_filter = StoreFilter(request.GET)
        all_stores = StoreFilter(request.GET).qs ## Query_set
    else:
        stores_filter = StoreFilter()
    
    print('all_stores')
    context = {
        'all_stores':all_stores,
        'stores_filter':stores_filter,
         
    }
    return render(request,'store/all_stores.html',context)
    
def store_detail(request,slug):
    try:
        store = get_object_or_404(Store,slug=slug)
        print(store)
    except:
        store = None
    
    context = {
         "store":store,
        }
    return render(request,'store/store_detail.html',context)



def create_store (request):
    form = CreateStoreForm()
    if request.method == "POST":
        form = CreateStoreForm(request.POST,request.FILES)
        if form.is_valid():
            #instance = ModelWithFileField(file_field=request.FILES['file'])
            #files = request.FILES.getlist('file_field')
            form.save()
            return redirect('all_stores')
        else:
            form = CreateStoreForm()
    context = {
        "title":"براند جديد",
        'form':form,
    }
    return render(request, 'store/create_store.html' ,context)















 