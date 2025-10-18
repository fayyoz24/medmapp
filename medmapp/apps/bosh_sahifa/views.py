from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import (Hudud, 
                    DavolashUsuli,
                    Konsultatsiya)
from .serializers import (HududSerializer, 
                        DavolashUsuliSerializer, 
                        KonsultatsiyaSerializer)           


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import KopTarmoqliTibbiyYordam, OmmabopShifoxonalar
from .serializers import KopTarmoqliTibbiyYordamSerializer, OmmabopShifoxonalarSerializer
from .throttles import PostPerDayThrottle

# ---------- HUDUD ----------
class HududListView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "uz")
        queryset = Hudud.objects.prefetch_related("translations").all()
        serializer = HududSerializer(queryset, many=True, context={"lang": lang})
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------- DAVOLASH USULLARI ----------
class DavolashUsuliListView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "uz")
        queryset = DavolashUsuli.objects.prefetch_related("translations").all()
        serializer = DavolashUsuliSerializer(queryset, many=True, context={"lang": lang})
        return Response(serializer.data, status=status.HTTP_200_OK)

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




# ---------- KO‘P TARMOQ TIBBIY YORDAM ----------
class KopTarmoqliTibbiyYordamListView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "uz")
        queryset = KopTarmoqliTibbiyYordam.objects.prefetch_related("translations").all()
        serializer = KopTarmoqliTibbiyYordamSerializer(queryset, many=True, context={"lang": lang})
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------- OMMABOP SHIFOXONALAR ----------
class OmmabopShifoxonalarListView(APIView):
    def get(self, request):
        lang = request.query_params.get("lang", "uz")
        queryset = OmmabopShifoxonalar.objects.prefetch_related("translations").all()
        serializer = OmmabopShifoxonalarSerializer(queryset, many=True, context={"lang": lang})
        return Response(serializer.data, status=status.HTTP_200_OK)


from rest_framework import generics, permissions
from .models import KafolatlanganArzonNarxlar, Natijalar
from .serializers import KafolatlanganArzonNarxlarSerializer, NatijalarSerializer


# ---------- KAFOLATLANGAN ARZON NARXLAR ----------
class KafolatlanganArzonNarxlarListView(generics.ListAPIView):
    queryset = KafolatlanganArzonNarxlar.objects.prefetch_related("translations").all()
    serializer_class = KafolatlanganArzonNarxlarSerializer
    permission_classes = [permissions.AllowAny]  # faqat GET


# ---------- NATIJALAR ----------
class NatijalarListView(generics.ListAPIView):
    queryset = Natijalar.objects.prefetch_related("translations").all()
    serializer_class = NatijalarSerializer
    permission_classes = [permissions.AllowAny]  # faqat GET


from rest_framework import generics, permissions
from .models import BizningXizmatlarEhtiyojQoplaydi, MashhurShifokorlar
from .serializers import (
    BizningXizmatlarEhtiyojQoplaydiSerializer,
    MashhurShifokorlarSerializer
)


# ===================== Bizning xizmatlar =====================
class BizningXizmatlarEhtiyojQoplaydiListView(generics.ListAPIView):
    queryset = BizningXizmatlarEhtiyojQoplaydi.objects.prefetch_related("translations").all()
    serializer_class = BizningXizmatlarEhtiyojQoplaydiSerializer
    permission_classes = [permissions.AllowAny]  # faqat GET


# ===================== Mashhur shifokorlar =====================
class MashhurShifokorlarListView(generics.ListAPIView):
    queryset = MashhurShifokorlar.objects.prefetch_related("translations").all()
    serializer_class = MashhurShifokorlarSerializer
    permission_classes = [permissions.AllowAny]  # faqat GET
