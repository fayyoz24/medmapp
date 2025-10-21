from django.urls import path
from .views import MamnunBemorView, BemorFikriView


urlpatterns = [
    path("mamnun-bemorlar/", MamnunBemorView.as_view(), name="mamnun-bemorlar"),
    path("bemor-fikrlari/", BemorFikriView.as_view(), name="bemor-fikrlari"),
]