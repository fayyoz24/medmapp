from django.urls import path
from .views import AsosiyYonalishListAPIView

urlpatterns = [
    path("asosiy-yonalishlar/", AsosiyYonalishListAPIView.as_view(), name="asosiy-yonalishlar"),
    
]