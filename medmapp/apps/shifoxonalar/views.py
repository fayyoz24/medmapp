from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Davlat, Shahar, Shifoxona
from .serializers import DavlatSerializer, ShaharSerializer, ShifoxonaSerializer


# ------------------ DAVLAT ------------------
class DavlatView(APIView):
    def get(self, request):
        queryset = Davlat.objects.prefetch_related("translations").all()
        serializer = DavlatSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


# ------------------ SHAHAR ------------------
class ShaharView(APIView):
    def get(self, request):
        davlat_id = request.query_params.get("davlat_id")
        queryset = Shahar.objects.prefetch_related("translations")
        if davlat_id:
            queryset = queryset.filter(davlat_id=davlat_id)
        serializer = ShaharSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


# ------------------ SHIFOXONA ------------------
class ShifoxonaView(APIView):
    def get(self, request):
        shahar_id = request.query_params.get("shahar_id")
        yonalish_id = request.query_params.get("asosiy_yonalish_id")

        queryset = Shifoxona.objects.prefetch_related("translations", "asosiy_yonalish", "shahar")

        if shahar_id:
            queryset = queryset.filter(shahar_id=shahar_id)
        if yonalish_id:
            queryset = queryset.filter(asosiy_yonalish__id=yonalish_id)

        serializer = ShifoxonaSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
