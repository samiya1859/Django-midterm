from django.shortcuts import render,redirect
from car.models import CarModel
from django.contrib.auth.decorators import login_required
from .models import Order
from django.contrib import messages
# Create your views here.
@login_required
def buy_car(request,id):
    car = CarModel.objects.get(pk=id)

    if car.quantity>0:
        order = Order(user=request.user,car=car,quantity=1,total_price=car.price)
        order.save()
        car.quantity-=1
        car.save()
        messages.success(request,'Car purchased successfully')
    else:
        messages.error(request,'Car out of stock')
    return redirect('home')
        