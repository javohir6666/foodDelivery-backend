from django.contrib import admin
from .models import Basket, BasketItem, Order, Feedback
# Register your models here.


admin.site.register(Basket)

admin.site.register(BasketItem)

admin.site.register(Order)

admin.site.register(Feedback)
