from django.urls import path
from . import views
urlpatterns = [
    path('addcar/',views.AddCarView.as_view(),name='add_car'),
    path('editcar/',views.EditCarView.as_view(),name='edit_car'),
    path('deletecar/',views.DeleteCarView.as_view(),name='delete_car'),
    path('detailcar/<int:id>',views.CarDetailView.as_view(),name='detail_car'),
    path('buy/<int:id>/',views.buy_car,name='buy_car'),
    path('order_history/',views.order_history,name='order_history'),
]
