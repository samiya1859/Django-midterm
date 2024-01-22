from django.db import models
from django.contrib.auth.models import User
from car.models import CarModel
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total_price = models.IntegerField()
    
