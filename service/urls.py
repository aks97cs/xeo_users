from django.urls import path, include
from service.views import User

urlpatterns = [
    path('user', User.as_view()),
]