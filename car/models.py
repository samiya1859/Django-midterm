from django.db import models
from brand.models import BrandModel
from django.contrib.auth.models import User 
# Create your models here.




class CarModel(models.Model):
    car_name = models.CharField(max_length=20)
    brand = models.ForeignKey(BrandModel, on_delete = models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to='car_images/')
    car_price = models.IntegerField()
    quantity = models.PositiveBigIntegerField(default=0)
    
    def __str__(self) :
        return self.car_name
    
class CommentModel(models.Model):
    car = models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments',null=True,blank=True)
    name = models.CharField(max_length = 20)
    comment = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"Comment by {self.name}"


class BuyingModel(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='users')
    cars = models.ManyToManyField(CarModel,related_name='cars') 
    quantity = models.IntegerField(default=0)
    