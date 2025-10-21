from django.urls import path
from .views import ShifoxonaView, YonalishAmaliyotiView


urlpatterns = [
    path("shifoxonalar/", ShifoxonaView.as_view(), name="shifoxonalar"),
    path("yonalish-amaliyotlari/", YonalishAmaliyotiView.as_view(), name="yonalish-amaliyotlari"),
]