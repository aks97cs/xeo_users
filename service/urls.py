from django.urls import path, include
from service.views import User

urlpatterns = [
    path('user', User.as_view(), name="user_api"),
    path('user/<int:id>', User.as_view(), name="user_api"),
]