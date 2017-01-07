# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-07 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Altname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='LOCATION.ALTNAME.NAME')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ALTNAME.SLUG')),
                ('is_preferred', models.BooleanField(default=True, verbose_name='LOCATION.ALTNAME.PREFERRED_NAME')),
                ('is_short', models.BooleanField(default=True, verbose_name='LOCATION.ALTNAME.SHORT')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('ref_geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ALTNAME.ACTIVE')),
            ],
            options={
                'verbose_name': 'LOCATION.ALTNAME',
                'db_table': 'geoware-altname',
                'verbose_name_plural': 'LOCATION.ALTNAME#plural',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('bbw', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.WEST')),
                ('bbn', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.NORTH')),
                ('bbe', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.EAST')),
                ('bbs', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.SOUTH')),
                ('lat', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.LATITUDE')),
                ('lng', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.LONGITUDE')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_city_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
            ],
            options={
                'verbose_name': 'LOCATION.CITY',
                'db_table': 'geoware-city',
                'verbose_name_plural': 'LOCATION.CITY#plural',
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('code', models.CharField(db_index=True, max_length=2, verbose_name='LOCATION.CONTINENT.CODE')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_continent_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
            ],
            options={
                'verbose_name': 'LOCATION.CONTINENT',
                'db_table': 'geoware-continent',
                'verbose_name_plural': 'LOCATION.CONTINENT#plural',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('code', models.CharField(db_index=True, max_length=2, verbose_name='LOCATION.CODE.ISO_ALPHA_2')),
                ('iso_3', models.CharField(db_index=True, max_length=3, verbose_name='LOCATION.CODE.ISO_ALPHA_3')),
                ('iso_n', models.CharField(db_index=True, max_length=40, verbose_name='LOCATION.CODE.ISO_NUMERIC')),
                ('fips', models.CharField(db_index=True, max_length=40, verbose_name='LOCATION.CODE.FIPS')),
                ('idc', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.CODE.INTERNATIONAL_DIALING')),
                ('tld', models.CharField(blank=True, max_length=2, null=True, verbose_name='LOCATION.CODE.TOP_LEVEL_DOMAIN')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_country_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_capital', to='geoware.City', verbose_name='LOCATION.CAPTIAL')),
                ('continent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_continent', to='geoware.Continent', verbose_name='LOCATION.COUNTRY.CONTINENT')),
            ],
            options={
                'verbose_name': 'LOCATION.COUNTRY',
                'db_table': 'geoware-country',
                'verbose_name_plural': 'LOCATION.COUNTRY#plural',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.CURRENCY.NAME')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.CURRENCY.SLUG')),
                ('code', models.CharField(db_index=True, max_length=40, verbose_name='LOCATION.CURRENCY.CODE')),
                ('symbol', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.CURRENCY.SYMBOL')),
                ('fractional_unit', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.CURRENCY.FRACTIONAL_UNIT')),
                ('fractional_ratio', models.PositiveIntegerField(default=0, verbose_name='LOCATION.CURRENCY.FRACTIONAL_RATIO')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.CURRENCY.URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='LOCATION.CURRENCY.INFO_DETAILS')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.CURRENCY.ACTIVE')),
            ],
            options={
                'verbose_name': 'LOCATION.CURRENCY',
                'db_table': 'geoware-currency',
                'verbose_name_plural': 'LOCATION.CURRENCY#plural',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('bbw', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.WEST')),
                ('bbn', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.NORTH')),
                ('bbe', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.EAST')),
                ('bbs', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.BOUNDING.BOX.SOUTH')),
                ('lat', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.LATITUDE')),
                ('lng', models.FloatField(default=0.0, verbose_name='LOCATION.CITY.LONGITUDE')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_district_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
                ('city', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_district_city', to='geoware.City', verbose_name='LOCATION.DISTRICT')),
            ],
            options={
                'verbose_name': 'LOCATION.DISTRICT',
                'db_table': 'geoware-district',
                'verbose_name_plural': 'LOCATION.DISTRICT#plural',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.LANGUAGE.NAME')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.LANGUAGE.SLUG')),
                ('code', models.CharField(db_index=True, max_length=40, verbose_name='LOCATION.LANGUAGE.CODE')),
                ('percent', models.FloatField(blank=True, null=True, verbose_name='LOCATION.LANGUAGE.WORLDWIDE_PERCENTAGE')),
                ('dialect', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.LANGUAGE.DIALECT')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.LANGUAGE.URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='LOCATION.LANGUAGE.INFO_DETAILS')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.LANGUAGE.ACTIVE')),
            ],
            options={
                'verbose_name': 'LOCATION.LANGUAGE',
                'db_table': 'geoware-language',
                'verbose_name_plural': 'LOCATION.LANGUAGE#plural',
            },
        ),
        migrations.CreateModel(
            name='Ocean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('depth', models.PositiveIntegerField(blank=True, null=True, verbose_name='LOCATION.OCEAN.DEPTH_MAX')),
                ('depth_name', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.OCEAN.DEPTH_MAX_NAME')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_ocean_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
            ],
            options={
                'verbose_name': 'LOCATION.OCEAN',
                'db_table': 'geoware-ocean',
                'verbose_name_plural': 'LOCATION.OCEAN#plural',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('code', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.REGION.CODE')),
                ('fips', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.REGION.CODE_FIPS')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_region_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_region_capital', to='geoware.City', verbose_name='LOCATION.REGION.CAPITAL')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_region_country', to='geoware.Country', verbose_name='LOCATION.REGION.COUNTRY')),
            ],
            options={
                'verbose_name': 'LOCATION.REGION',
                'db_table': 'geoware-region',
                'verbose_name_plural': 'LOCATION.REGION#plural',
            },
        ),
        migrations.CreateModel(
            name='Subregion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.SLUG')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.NAME_STD.FIELD')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='LOCATION.AREA_SQUARE_KM')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='LOCATION.POPULATION')),
                ('elevation', models.PositiveIntegerField(default=0, verbose_name='LOCATION.ELEVATION_METERS')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.URL')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('info', models.TextField(blank=True, verbose_name='LOCATION.INFO')),
                ('absolute_url', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.ABS.URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.ACTIVE')),
                ('code', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.SUBREGION.CODE')),
                ('fips', models.CharField(blank=True, max_length=40, null=True, verbose_name='LOCATION.SUBREGION.CODE_FIPS')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_subregion_altnames', to='geoware.Altname', verbose_name='LOCATION.ALTNAME')),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_subregion_capital', to='geoware.City', verbose_name='LOCATION.SUBREGION.CAPITAL')),
                ('region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_subregion_country', to='geoware.Region', verbose_name='LOCATION.SUBREGION.REGION')),
            ],
            options={
                'verbose_name': 'LOCATION.SUBREGION',
                'db_table': 'geoware-subregion',
                'verbose_name_plural': 'LOCATION.SUBREGION#plural',
            },
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name_id', models.CharField(db_index=True, max_length=254, verbose_name='LOCATION.TIMEZONE.ID')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='LOCATION.TIMEZONE.SLUG')),
                ('gmt_offset', models.FloatField(default=0.0, verbose_name='LOCATION.TIMEZONE.OFFSET_GMT_JAN_1')),
                ('dst_offset', models.FloatField(default=0.0, verbose_name='LOCATION.TIMEZONE.OFFSET_DST_JUL_1')),
                ('raw_offset', models.FloatField(default=0.0, verbose_name='LOCATION.TIMEZONE.OFFSET_RAW')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='LOCATION.TIMEZONE.URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='LOCATION.TIMEZONE.INFO_DETAILS')),
                ('is_active', models.BooleanField(default=True, verbose_name='LOCATION.TIMEZONE.ACTIVE')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_timezone_country', to='geoware.Country', verbose_name='LOCATION.TIMEZONE.COUNTRY')),
            ],
            options={
                'verbose_name': 'LOCATION.TIMEZONE',
                'db_table': 'geoware-timezone',
                'verbose_name_plural': 'LOCATION.TIMEZONE#plural',
            },
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='currency',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AddField(
            model_name='country',
            name='currency',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_currency', to='geoware.Currency', verbose_name='LOCATION.CURRENCY'),
        ),
        migrations.AddField(
            model_name='country',
            name='jurisdiction',
            field=models.ForeignKey(blank=True, help_text='LOCATION.COUNTRY.SOVEREIGNTY', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_jurisdiction', to='geoware.Country', verbose_name='LOCATION.COUNTRY.JURISDICTION'),
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='geoware_country_languagues', to='geoware.Language', verbose_name='LOCATION.LANGUAGUES'),
        ),
        migrations.AddField(
            model_name='country',
            name='neighbors',
            field=models.ManyToManyField(blank=True, related_name='_country_neighbors_+', to='geoware.Country', verbose_name='LOCATION.NEIGHBORS'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_country', to='geoware.Country', verbose_name='LOCATION.CITY.COUNTRY'),
        ),
        migrations.AddField(
            model_name='city',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_region', to='geoware.Region', verbose_name='LOCATION.CITY.REGION'),
        ),
        migrations.AddField(
            model_name='city',
            name='sister',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geoware.City', verbose_name='LOCATION.CITY.SISTER'),
        ),
        migrations.AddField(
            model_name='city',
            name='subregion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_subregion', to='geoware.Subregion', verbose_name='LOCATION.CITY.SUBREGION'),
        ),
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_timezone', to='geoware.Timezone', verbose_name='LOCATION.CITY.TIMEZONE'),
        ),
        migrations.AddField(
            model_name='altname',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_altname_language', to='geoware.Language', verbose_name='LOCATION.ALTNAME.LAGUAGUE'),
        ),
        migrations.AlterUniqueTogether(
            name='subregion',
            unique_together=set([('name', 'fips', 'region')]),
        ),
        migrations.AlterUniqueTogether(
            name='region',
            unique_together=set([('fips', 'name_std', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='district',
            unique_together=set([('name', 'city')]),
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='continent',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'region', 'country')]),
        ),
    ]
