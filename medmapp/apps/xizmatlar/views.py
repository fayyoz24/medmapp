from django.shortcuts import render

# Create your views here.
from bosh_sahifa.serializers import AsosiyYonalishSerializer
from bosh_sahifa.models import AsosiyYonalish
from bosh_sahifa.views import CACHE_TTL, cache_page
from django.utils.decorators import method_decorator
from rest_framework import generics
from django.views.decorators.cache import cache_page



@method_decorator(cache_page(CACHE_TTL), name='dispatch')
class AsosiyYonalishListAPIView(generics.ListAPIView):
    queryset = AsosiyYonalish.objects.prefetch_related("translations").all()
    serializer_class = AsosiyYonalishSerializer