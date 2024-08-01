from django.db import models
from users.models import CustomUser

class FoodType(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/food_types/', default='images/food_types/default.png')

    def __str__(self):
        return self.name

class Category(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class FoodItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/foods/', default='images/foods/default.png')
    weight = models.FloatField(default=0, blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supplier = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
