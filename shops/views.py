
from django.http import Http404
from django.shortcuts import render
from .models import IceCream
# Create your views here.

def get_ice_cream (request,ice_cream_id):
    try:
        ice_cream = IceCream.objects.get(id=ice_cream_id)
    except IceCream.DoesNotExist:
        raise Http404("Ice Cream does not exists")
    context = {
       "ice_cream":{
           "id":ice_cream.id,
        "name": ice_cream.name,
        "shop": ice_cream.shop.name,
        "stock": str(ice_cream.stock)
        }
       
    }
    return render(request, "ice_cream_detail.html", context)


def get_ice_creams(request):
    ice_creams = IceCream.objects.all()
    context = {
        "ice_creams": ice_creams
    }
    return render(request, "ice_cream_list.html", context)