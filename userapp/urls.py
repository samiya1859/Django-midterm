from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.UserLoginView.as_view(),name='user_login'),
    path('logout/',views.user_logout,name='user_logout'),
    path('signup/',views.SignupView.as_view(),name='signup'),
    path('profile/<int:id>',views.Profileview.as_view(),name='profile'),
    path('profile/edit/',views.edit_profile,name='edit_profile'),
    path('profile/edit/passchange',views.pass_change,name='passchange'),
    
]
