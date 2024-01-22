from django.shortcuts import render,redirect,get_object_or_404
from brand.models import BrandModel
from car.models import CarModel,BuyingModel


def home(request, brand_slug=None):
    data = CarModel.objects.all()
    brands = BrandModel.objects.all()
    orders = BuyingModel.objects.all()
    if brand_slug is not None:
        # brand = BrandModel.objects.get(slug=brand_slug)
        brand = get_object_or_404(BrandModel, slug=brand_slug)
        data = CarModel.objects.filter(brand=brand)
    
    return render(request,'home.html',{'data':data,'brand':brands,'orders':orders})       


