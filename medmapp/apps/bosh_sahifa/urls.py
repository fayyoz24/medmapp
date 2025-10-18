from django.urls import path

from django.urls import path
from .views import (HududListView, 
                DavolashUsuliListView, 
                KonsultatsiyaCreateView,
                KopTarmoqliTibbiyYordamListView,
                OmmabopShifoxonalarListView,
                KafolatlanganArzonNarxlarListView,
                NatijalarListView,
                BizningXizmatlarEhtiyojQoplaydiListView,
                MashhurShifokorlarListView)


urlpatterns = [
    path("hududlar/", HududListView.as_view(), name="hududlar"),
    path("davolash-usullari/", DavolashUsuliListView.as_view(), name="davolash_usullari"),
    path("konsultatsiya/", KonsultatsiyaCreateView.as_view(), name="konsultatsiya_create"),
    path("kop-tarmoqli-tibbiy-yordamlar/", KopTarmoqliTibbiyYordamListView.as_view(), name="kop_tibbiy_yordamlar"),
    path("ommabop-shifoxonalar/", OmmabopShifoxonalarListView.as_view(), name="ommabop_shifoxonalar"),
    path("kafolatlangan-narxlar/", KafolatlanganArzonNarxlarListView.as_view(), name="kafolatlangan_narxlar"),
    path("natijalar/", NatijalarListView.as_view(), name="natijalar"),
    path("bizning-xizmatlar/", BizningXizmatlarEhtiyojQoplaydiListView.as_view(), name="bizning_xizmatlar"),
    path("mashhur-shifokorlar/", MashhurShifokorlarListView.as_view(), name="mashhur_shifokorlar"),
]
