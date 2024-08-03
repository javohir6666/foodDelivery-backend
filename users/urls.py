from django.urls import path
from .views import register_user, logout, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('logout/', logout, name='logout'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]