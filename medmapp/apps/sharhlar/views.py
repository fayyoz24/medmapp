from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import MamnunBemor, BemorFikri
from .serializers import MamnunBemorSerializer, BemorFikriSerializer


class MamnunBemorView(APIView):
    """Return satisfaction statistics (mamnun bemorlar)."""
    def get(self, request):
        queryset = MamnunBemor.objects.all().order_by("-id")
        serializer = MamnunBemorSerializer(queryset, many=True)
        return Response(serializer.data)


class BemorFikriView(APIView):
    """Return patients' feedbacks (bemorlar fikrlari)."""
    def get(self, request):
        queryset = BemorFikri.objects.select_related(
            "bemor", "shifoxona", "amaliyot"
        ).order_by("-yaratilgan_sana")

        serializer = BemorFikriSerializer(queryset, many=True, context={"request": request})
        return Response(serializer.data)
