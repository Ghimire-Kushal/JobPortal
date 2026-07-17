from .views import HomeAPIView
from django.urls import path

urlpatterns = [
    path("home/",HomeAPIView.as_view(),
        name="home-api-view")
]