from django.urls import path
from service.views import User
from service.views import Auth

urlpatterns = [
    path('auth', Auth.as_view(), name='user_auth'),
    path('register', User.as_view(), name="user_api"),
    path('info/<uuid:id>', User.as_view(), name="user_api_args"),
    path('password-reset/<int:id>', User.as_view(), name="user_api_args"),
]
