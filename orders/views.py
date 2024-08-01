from rest_framework import viewsets
from .models import Basket, BasketItem, Order, Feedback
from .serializers import BasketSerializer, BasketItemSerializer, OrderSerializer, FeedbackSerializer

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
