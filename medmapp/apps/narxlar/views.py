from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from bosh_sahifa.models import YonalishAmaliyoti
from shifoxonalar.models import Shifoxona
from .serializers import ShifoxonaSerializer, YonalishAmaliyotiSerializer
    

class YonalishAmaliyotiView(APIView):
    def get(self, request):
        asosiy_yonalish_id = request.query_params.get("asosiy_yonalish")

        queryset = YonalishAmaliyoti.objects.prefetch_related(
            "translations", "asosiy_yonalish"
        ).all()

        if asosiy_yonalish_id:
            queryset = queryset.filter(asosiy_yonalish_id=asosiy_yonalish_id)

        serializer = YonalishAmaliyotiSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)


class ShifoxonaView(APIView):
    def get(self, request):
        asosiy_yonalish_id = request.query_params.get("asosiy_yonalish_id")
        amaliyot_yonalish_id = request.query_params.get("amaliyot_yonalish_id")

        queryset = Shifoxona.objects.prefetch_related("translations", "asosiy_yonalish", "shahar")

        # CASE 1: asosiy_yonalish_id
        if asosiy_yonalish_id:
            queryset = queryset.filter(asosiy_yonalish__id=asosiy_yonalish_id)

        # CASE 2: amaliyot_yonalish_id
        elif amaliyot_yonalish_id:
            amaliyot = YonalishAmaliyoti.objects.filter(id=amaliyot_yonalish_id).first()
            if amaliyot:
                queryset = queryset.filter(asosiy_yonalish=amaliyot.asosiy_yonalish)

        # else: return all

        serializer = ShifoxonaSerializer(queryset.distinct(), many=True, context={"request": request})
        return Response(serializer.data)
