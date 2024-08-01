from django.db import models
from users.models import CustomUser
from food.models import FoodItem

status_choices =[
    ("1", 'Preparing'),          
    ("2", 'Out for delivery'),          
    ("3", 'Delivered')
]

class Basket(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(FoodItem, through='BasketItem')

class BasketItem(models.Model):
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE)
    food_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    basket = models.OneToOneField(Basket, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices = status_choices)
    ordered_at = models.DateTimeField(auto_now_add=True)

class Feedback(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    comment = models.TextField()
