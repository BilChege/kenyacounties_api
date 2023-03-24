from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import Subcounty

class SubcountySerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Subcounty
        geo_field = "geom"
        fields = '__all__'

class CountySerializer(serializers.Serializer):
    county = serializers.CharField(max_length=200)
    adm1_pcode = serializers.CharField(max_length=5)
    adm0_en = serializers.CharField(max_length=5)
    adm0_pcode = serializers.CharField(max_length=2)
    type_field = serializers.CharField(max_length=9)
    date_field = serializers.CharField(max_length=10)
    # adminarea = serializers.CharField(max_length=9)