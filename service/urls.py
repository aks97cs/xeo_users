from django.urls import path, include
from service.views import User
from service.views import CustomAuthToken

urlpatterns = [
    path('user/auth', CustomAuthToken.as_view(), name='user_auth'),
    path('user', User.as_view(), name="user_api"),
    path('user/<int:id>', User.as_view(), name="user_api"),
]