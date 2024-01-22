
from django.shortcuts import render,redirect
from . import forms
from car.models import CarModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView,TemplateView,UpdateView,DetailView
from django.urls import reverse_lazy
# Create your views here.


class SignupView(CreateView):
    model = User
    form_class= forms.SignUpForm
    template_name = 'signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request,'SignUp successfully')
        return response

class UserLoginView(LoginView):
    template_name = 'login.html'
    def get_success_url(self):
        return reverse_lazy('home')
    def form_valid(self, form):
        messages.success(self.request,'Logged in successfully')
        return super().form_valid(form)
    def form_invalid(self, form):
        messages.warning(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    

@login_required
def profile(request):
    data = CarModel.objects.filter(userapp = request.user)
    return render(request,'profile.html',{'data':data})

class Profileview(DetailView):
    model = User
    template_name = 'profile.html'
    context_object_name='user'
    success_url = reverse_lazy('profile')
    pk_url_kwarg= 'id'

# class ProfileEditView(UpdateView):
#     model = User
#     form_class = forms.ChangeUserForm
#     template_name = 'editprofile.html'
#     success_url = reverse_lazy('profile')
#     pk_url_kwarg = 'id'

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated Successfully')
            return redirect('edit_profile')
    
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'editprofile.html', {'form' : profile_form})


def user_logout(request):
    logout(request)
    messages.success(request,'Logged out successfully')
    return redirect('home')

def pass_change(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Password Updated successfully!')
            return redirect('profile')
    else:
        form=PasswordChangeForm(user=request.user)
    return render(request,'pass_change.html',{'form':form})


