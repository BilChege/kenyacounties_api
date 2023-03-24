# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

# Create your models here.

class Subcounty(models.Model):
    adm1_pcode = models.CharField(max_length=5)
    subcounty = models.CharField(max_length=17)
    adminarea = models.CharField(max_length=9)
    openbush = models.FloatField()
    county = models.CharField(max_length=15)
    adm2_pcode = models.CharField(max_length=8)
    adm0_en = models.CharField(max_length=5)
    shape_leng = models.FloatField()
    adm1_en = models.CharField(max_length=15)
    validon = models.CharField(max_length=10)
    adm2_en = models.CharField(max_length=19)
    shape_area = models.FloatField()
    adm0_pcode = models.CharField(max_length=2)
    shape_are = models.FloatField()
    shape_len = models.FloatField()
    type_field = models.CharField(max_length=9)
    date_field = models.CharField(max_length=10)
    fid_field = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)


# Auto-generated `LayerMapping` dictionary for Subcounty model
subcounty_mapping = {
    'adm1_pcode': 'ADM1_PCODE',
    'subcounty': 'SubCounty',
    'adminarea': 'AdminArea',
    'openbush': 'OpenBush',
    'county': 'County',
    'adm2_pcode': 'ADM2_PCODE',
    'adm0_en': 'ADM0_EN',
    'shape_leng': 'Shape_Leng',
    'adm1_en': 'ADM1_EN',
    'validon': 'validOn',
    'adm2_en': 'ADM2_EN',
    'shape_area': 'Shape_Area',
    'adm0_pcode': 'ADM0_PCODE',
    'shape_are': 'Shape_Are',
    'shape_len': 'Shape_Len',
    'type_field': 'Type_',
    'date_field': 'date_',
    'fid_field': 'FID_',
    'geom': 'MULTIPOLYGON',
}