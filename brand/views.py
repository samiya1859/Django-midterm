from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render,redirect
from . import forms
from . import models
from car.models import CarModel
from django.urls import reverse_lazy
from django.views.generic import CreateView
# Create your views here.

class BrandCreateView(CreateView):
    model = models.BrandModel
    form_class = forms.BrandModelForm
    template_name = 'addBrand.html'
    success_url = reverse_lazy('add_brand')

    def form_valid(self, form):
        form.instance.userapp = self.request.user
        return super().form_valid(form)
    

def add_brand(request):
    if request.method=='POST':
        brand_form = forms.BrandModelForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return redirect('add_brand')
    else:
        brand_form=forms.BrandModelForm()
    return render(request,'addBrand.html',{'form':brand_form})
