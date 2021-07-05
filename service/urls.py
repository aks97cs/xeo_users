from django.urls import path
from service.views import User
from service.views import Auth

urlpatterns = [
    path('user/auth', Auth.as_view(), name='user_auth'),
    path('user', User.as_view(), name="user_api"),
    path('user/<int:id>', User.as_view(), name="user_api_args"),
]
