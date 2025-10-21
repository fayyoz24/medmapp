
from django.urls import path
from .views import (
    HududListAPIView, 
    AsosiyYonalishListAPIView, 
    YonalishAmaliyotiListAPIView,
    NatijalarListAPIView, 
    BizningXizmatlarListAPIView, 
    KonsultatsiyaCreateView,
    DavolashUsuliTanlangListAPIView
)

urlpatterns = [
    path("hududlar/", HududListAPIView.as_view(), name="hududlar"),
    path("konsultatsiya-create/", KonsultatsiyaCreateView.as_view(), name="konsultatsiya_create"),
    path("asosiy-yonalishlar/", AsosiyYonalishListAPIView.as_view(), name="asosiy-yonalishlar"),
    path("yonalish-amaliyotlari/", YonalishAmaliyotiListAPIView.as_view(), name="yonalish-amaliyotlari"),
    path("natijalar/", NatijalarListAPIView.as_view(), name="natijalar"),
    path("bizning-xizmatlar/", BizningXizmatlarListAPIView.as_view(), name="bizning-xizmatlar"),
    path("davolash-usullari/", DavolashUsuliTanlangListAPIView.as_view(), name="davolash-usullari"),
]
