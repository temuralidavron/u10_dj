from xml.etree.ElementInclude import include

from django.shortcuts import render, redirect
from .models import Phone
# Create your views here.


#crud create,read(hammisini oqish,id oqish),update,delete
# list
def list_phone(request):
    print("nima gaaaap")
    tellar=Phone.objects.all()
    context={
        'phones':tellar
    }
    return render(request,"phone/list.html",context)

# create

def create_phone(request):
    if request.method=='POST':
        brand=request.POST.get('brand')
        model=request.POST.get('model')
        price=request.POST.get('price')
        quantity=request.POST.get('quantity')
        image=request.FILES.get('image')
        description=request.POST.get("description")
        if brand and model and price and quantity and description:
            Phone.objects.create(
                brand=brand,
                model=model,
                price=price,
                quantity=quantity,
                image=image,
                description=description
            )
            return redirect("list")
    return render(request,"phone/create.html",)




def detail_phone(request,pk):
    phone=Phone.objects.get(pk=pk)  # select * from phone where pk=pk
    return render(request,'phone/detail.html',{'phone':phone})

def phone_update(request,pk):
    phone=Phone.objects.filter(pk=pk).first()
    if request.method=='POST':
        brand = request.POST.get('brand',phone.brand)
        model = request.POST.get('model',phone.model)
        price = request.POST.get('price',phone.price)
        quantity = request.POST.get('quantity',phone.quantity)
        image = request.FILES.get('image')
        description = request.POST.get("description",phone.description)
        if brand and model and price:
            phone.brand=brand
            phone.model=model
            phone.price=price
            phone.quantity=quantity
            phone.image=image
            phone.description=description
            phone.save()
            return redirect('list')
    return render(request,"phone/create.html",{'phone':phone})
