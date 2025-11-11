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
        if brand and model and price and quantity:
            Phone.objects.create(
                brand=brand,
                model=model,
                price=price,
                quantity=quantity,
                image=image
            )
            return redirect("list")
    return render(request,"phone/create.html",)