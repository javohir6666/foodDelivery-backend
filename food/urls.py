from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from food.views import FoodTypeViewSet, CategoryViewSet, FoodItemViewSet
from .views import FoodTypeListCreateView, CategoryListCreateView, FoodItemListCreateView
from orders.views import BasketViewSet, OrderViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'foodtypes', FoodTypeViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'fooditems', FoodItemViewSet)
router.register(r'baskets', BasketViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'feedbacks', FeedbackViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
