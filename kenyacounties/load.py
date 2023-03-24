import os
from django.contrib.gis.utils import LayerMapping
from .models import Subcounty

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

subcounty_shapefile = 'E:\kenyasubcounties\subcountiesshapefiles\kensubc.shp'

def run(verbose=True):
    layermap = LayerMapping(Subcounty,subcounty_shapefile,subcounty_mapping,transform=False)
    layermap.save(strict=True,verbose=verbose)