from django.shortcuts import render
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Subcounty
from django.contrib.gis.geos import Point
from .serializers import SubcountySerializer, CountySerializer, PointSerializer
import math
from datetime import datetime
# Create your views here.

@api_view(['GET'])
def allCounties(request):
    sc = Subcounty.objects.values('county').distinct().values('county','adm1_pcode','adm0_en','adm0_pcode','type_field','date_field')
    serializer = CountySerializer(sc, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def subcountiesInCounty(request):
    countyparam = request.GET.get('county')
    sc = Subcounty.objects.filter(county = countyparam)
    serializer = SubcountySerializer(sc, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def subcountyForPoint(request):
    print(request.data)    
    lat = request.data.get('latitude')
    lon = request.data.get('longitude')
    pnt = Point(lat,lon)
    queryset = Subcounty.objects.filter(geom__contains=pnt)
    sc = queryset[0]
    serializer = SubcountySerializer(sc)
    return Response(serializer.data)        