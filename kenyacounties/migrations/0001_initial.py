# Generated by Django 4.1.7 on 2023-03-18 09:54

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Subcounty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adm1_pcode', models.CharField(max_length=5)),
                ('subcounty', models.CharField(max_length=17)),
                ('adminarea', models.CharField(max_length=9)),
                ('openbush', models.FloatField()),
                ('county', models.CharField(max_length=15)),
                ('adm2_pcode', models.CharField(max_length=8)),
                ('adm0_en', models.CharField(max_length=5)),
                ('shape_leng', models.FloatField()),
                ('adm1_en', models.CharField(max_length=15)),
                ('validon', models.CharField(max_length=10)),
                ('adm2_en', models.CharField(max_length=19)),
                ('shape_area', models.FloatField()),
                ('adm0_pcode', models.CharField(max_length=2)),
                ('shape_are', models.FloatField()),
                ('shape_len', models.FloatField()),
                ('type_field', models.CharField(max_length=9)),
                ('date_field', models.CharField(max_length=10)),
                ('fid_field', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]
