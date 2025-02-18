from django.urls import path
from .views import UserRegistrationView, UserLoginView, api_test

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('api/test/', api_test, name='api_test'),
]
