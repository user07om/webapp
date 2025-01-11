from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.HelloUser.as_view(), name="home"),
]
