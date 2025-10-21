from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.conf import settings
from .models import (
    Hudud, AsosiyYonalish, YonalishAmaliyoti, Natijalar,
    BizningXizmatlarEhtiyojQoplaydi, DavolashUsuliTanlang
)
from .serializers import (
    HududSerializer, AsosiyYonalishSerializer, 
    YonalishAmaliyotiSerializer,
    NatijalarSerializer, 
    BizningXizmatlarSerializer, 
    DavolashUsuliTanlangSerializer,
    KonsultatsiyaSerializer
)
from rest_framework.views import APIView
from .throttles import PostPerDayThrottle
CACHE_TTL = getattr(settings, 'CACHE_TTL', 60 * 15)  # 15 minutes default cache
from rest_framework.response import Response
from rest_framework import status   
from django.views.decorators.vary import vary_on_headers

# # ========== HUDUD ==========
# @method_decorator(vary_on_headers("Accept-Language"), name="dispatch")
# @method_decorator(cache_page(CACHE_TTL, key_prefix="hudud"), name="dispatch")
class HududListAPIView(generics.ListAPIView):
    queryset = Hudud.objects.prefetch_related("translations").all()
    serializer_class = HududSerializer


# ========== ASOSIY YO‘NALISH ==========
# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AsosiyYonalishListAPIView(generics.ListAPIView):
    queryset = AsosiyYonalish.objects.prefetch_related("translations").all()
    serializer_class = AsosiyYonalishSerializer


# ========== YONALISH AMALIYOTI ==========
# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class YonalishAmaliyotiListAPIView(generics.ListAPIView):
    queryset = YonalishAmaliyoti.objects.prefetch_related("translations").all()
    serializer_class = YonalishAmaliyotiSerializer


# ========== NATIJALAR ==========
# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class NatijalarListAPIView(generics.ListAPIView):
    queryset = Natijalar.objects.prefetch_related("translations").all()
    serializer_class = NatijalarSerializer


# ========== BIZNING XIZMATLAR ==========
# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class BizningXizmatlarListAPIView(generics.ListAPIView):
    queryset = BizningXizmatlarEhtiyojQoplaydi.objects.prefetch_related("translations").all()
    serializer_class = BizningXizmatlarSerializer


# ========== DAVOLASH USULI TANLANG ==========
# @method_decorator(cache_page(CACHE_TTL), name='dispatch')
class DavolashUsuliTanlangListAPIView(generics.ListAPIView):
    queryset = DavolashUsuliTanlang.objects.prefetch_related("translations", "shifoxona", "doktor").all()
    serializer_class = DavolashUsuliTanlangSerializer


# ---------- KONSULTATSIYA YUBORISH ----------
class KonsultatsiyaCreateView(APIView):
    throttle_classes = [PostPerDayThrottle]
    def post(self, request):
        serializer = KonsultatsiyaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Konsultatsiya so‘rovi muvaffaqiyatli yuborildi!"},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
