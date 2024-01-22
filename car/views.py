
from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse_lazy
from . import forms
from .models import CarModel,BuyingModel
from django.views.generic import CreateView,UpdateView,DetailView,DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@method_decorator(login_required,name='dispatch')
class AddCarView(CreateView):
    model =CarModel
    form_class = forms.CarModelForm
    template_name = 'addCar.html'
    success_url = reverse_lazy('add_car')
    def form_valid(self, form):
        form.instance.userapp = self.request.user
        return super().form_valid(form)
    

class EditCarView(UpdateView):
    model = CarModel
    form_class = forms.CarModelForm
    template_name = 'addCar.html'
    pk_url_kwarg='id'
    success_url = reverse_lazy('edit_car')

class DeleteCarView(DeleteView):
    model = CarModel
    template_name = 'deleteCar.html'
    success_url= reverse_lazy('home')
    pk_url_kwarg='id'

class CarDetailView(DetailView):
    model = CarModel
    context_object_name = 'car'
    pk_url_kwarg = 'id'
    template_name = 'carDetails.html'

    def post(self,request,*args,**kwargs):
        comment_form = forms.CommentForm(data=self.request.POST)
        car = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.car=car
            new_comment.save()
            
        return self.get(request,*args,**kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        comments = car.comments.all()
        comment_form = forms.CommentForm()
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context

# @login_required
# def buy_car(request,id):
#     car = CarModel.objects.get(pk=id)
#     order = BuyingModel.objects.get(pk=id)
#     if car.quantity>0:
#         car.quantity-=1
#         order.quantity+=1
#         car.save()
#         users,created = BuyingModel.objects.get_or_create(user=request.user)

#         # Associate the purchased car with the BuyingModel
#         users.cars.add(car)
#         messages.success(request,'Car purchased successfully')
#     else:
#         messages.error(request,'Car out of stock')
#     return redirect('profile', id = request.user.id)


        

# @login_required
# def buy_car(request, id):
#     car = get_object_or_404(CarModel, pk=id)
#     order, created = BuyingModel.objects.get_or_create(user=request.user)

#     if car.quantity > 0:
#         car.quantity -= 1
#         car.save()
#         order.cars.add(car)
#         order.quantity += 1
#         order.save()

#         messages.success(request, 'Car purchased successfully')
        
#         # Redirect to the car detail page with the car's ID
#         return redirect('detail_car', id=id)
#     else:
#         messages.error(request, 'Car out of stock')
#         return redirect('home')
    
@login_required
def buy_car(request, id):
    car = CarModel.objects.get(pk=id)
    user_profile, created = BuyingModel.objects.get_or_create(user=request.user)
    # print(created)
    # Check if the user has already this car then we hould increase quantity but first e check korte hobe j ei user er ei car ache kina age
    order_item = user_profile.cars.filter(pk=car.id).first()

    if order_item:
        # If the user already has this car, increase the quantity
        if car.quantity > 0:
            car.quantity -= 1
            order_item.quantity += 1
            car.save()
            order_item.save()
            messages.success(request, 'Car purchased successfully')
        else:
            messages.error(request, 'Car out of stock')
    else:
        # If the user doesn't have this car, add it to the order history
        if car.quantity > 0:
            car.quantity -= 1
            user_profile.cars.add(car, through_defaults={'quantity': 1})
            car.save()
            messages.success(request, 'Car purchased successfully')
        else:
            messages.error(request, 'Car out of stock')
    return redirect('profile', id=request.user.id)


def order_history(request):
    orders = request.user.users.cars.all()
    return render(request,'orderHistory.html',{'data':orders})