from django.contrib import admin
from .models import FoodItem, FoodType, Category
# Register your models here.
admin.site.register(FoodItem)
admin.site.register(FoodType)
admin.site.register(Category)