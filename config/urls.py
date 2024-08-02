from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet
from food.views import FoodTypeViewSet, CategoryViewSet, FoodItemViewSet
from orders.views import BasketViewSet, OrderViewSet, FeedbackViewSet
from django.conf import settings
from django.conf.urls.static import static


from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Food Delivery Project",
        default_version='v1',
        description="Food Delivery Project",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="admin@test.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


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
    path('user/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
