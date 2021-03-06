# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-27 15:34
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
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('ref_geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True)),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Altnames',
                'verbose_name': 'Altname',
                'db_table': 'geoware-altname',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='Standard Name')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='Area (Square KM)')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='Population')),
                ('elevation', models.IntegerField(default=0, verbose_name='Elevation')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('bbw', models.FloatField(default=0.0, verbose_name='Bounding Box West')),
                ('bbn', models.FloatField(default=0.0, verbose_name='Bounding Box North')),
                ('bbe', models.FloatField(default=0.0, verbose_name='Bounding Box East')),
                ('bbs', models.FloatField(default=0.0, verbose_name='Bounding Box South')),
                ('lat', models.FloatField(default=0.0, verbose_name='Latitude')),
                ('lng', models.FloatField(default=0.0, verbose_name='Longitude')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_city_altnames', to='geoware.Altname', verbose_name='Altname')),
            ],
            options={
                'verbose_name_plural': 'Cities',
                'verbose_name': 'City',
                'db_table': 'geoware-city',
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='Standard Name')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='Area (Square KM)')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='Population')),
                ('elevation', models.IntegerField(default=0, verbose_name='Elevation')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('code', models.CharField(db_index=True, max_length=2, verbose_name='Code')),
                ('iso_n', models.CharField(blank=True, db_index=True, max_length=3, null=True, verbose_name='M49')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_continent_altnames', to='geoware.Altname', verbose_name='Altname')),
            ],
            options={
                'verbose_name_plural': 'Continents',
                'verbose_name': 'Continent',
                'db_table': 'geoware-continent',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='Standard Name')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='Area (Square KM)')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='Population')),
                ('elevation', models.IntegerField(default=0, verbose_name='Elevation')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('code', models.CharField(db_index=True, max_length=2, verbose_name='ISO 3166-1')),
                ('iso_3', models.CharField(db_index=True, max_length=3, verbose_name='ISO 3166-2')),
                ('iso_n', models.CharField(db_index=True, max_length=40, verbose_name='M49')),
                ('fips', models.CharField(db_index=True, max_length=40, verbose_name='FIPS')),
                ('idc', models.CharField(blank=True, max_length=40, null=True, verbose_name='International Dialing Code')),
                ('tld', models.CharField(blank=True, max_length=2, null=True, verbose_name='Top Level Domain')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_country_altnames', to='geoware.Altname', verbose_name='Altname')),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_capital', to='geoware.City', verbose_name='Capital')),
                ('continent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_continent', to='geoware.Continent', verbose_name='Continent')),
            ],
            options={
                'verbose_name_plural': 'Countries',
                'verbose_name': 'Country',
                'db_table': 'geoware-country',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('code', models.CharField(db_index=True, max_length=40, verbose_name='Code')),
                ('symbol', models.CharField(blank=True, max_length=40, null=True, verbose_name='Symbol')),
                ('fractional_unit', models.CharField(blank=True, max_length=40, null=True, verbose_name='Fractional Unit')),
                ('fractional_ratio', models.PositiveIntegerField(default=0, verbose_name='Fractional Ration')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Currencies',
                'verbose_name': 'Currency',
                'db_table': 'geoware-currency',
            },
        ),
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='Standard Name')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='Area (Square KM)')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='Population')),
                ('elevation', models.IntegerField(default=0, verbose_name='Elevation')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('code', models.CharField(blank=True, max_length=40, null=True, verbose_name='Code')),
                ('fips', models.CharField(blank=True, max_length=40, null=True, verbose_name='FIPS')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_division_altnames', to='geoware.Altname', verbose_name='Altname')),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_division_capital', to='geoware.City', verbose_name='Capital')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_division_country', to='geoware.Country', verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Divisions',
                'verbose_name': 'Division',
                'db_table': 'geoware-division',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(blank=True, max_length=254, null=True, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('code', models.CharField(db_index=True, max_length=40, verbose_name='Code')),
                ('percent', models.FloatField(blank=True, null=True, verbose_name='Worldwide Percentage')),
                ('dialect', models.CharField(blank=True, max_length=254, null=True, verbose_name='Dialect')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
            ],
            options={
                'verbose_name_plural': 'Languages',
                'verbose_name': 'Language',
                'db_table': 'geoware-language',
            },
        ),
        migrations.CreateModel(
            name='Ocean',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='Standard Name')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='Area (Square KM)')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='Population')),
                ('elevation', models.IntegerField(default=0, verbose_name='Elevation')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('depth', models.PositiveIntegerField(blank=True, null=True, verbose_name='Depth')),
                ('depth_name', models.CharField(blank=True, max_length=254, null=True, verbose_name='Depth Name')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_ocean_altnames', to='geoware.Altname', verbose_name='Altname')),
            ],
            options={
                'verbose_name_plural': 'Oceans',
                'verbose_name': 'Ocean',
                'db_table': 'geoware-ocean',
            },
        ),
        migrations.CreateModel(
            name='Subdivision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('name_std', models.CharField(blank=True, max_length=254, null=True, verbose_name='Standard Name')),
                ('area', models.PositiveIntegerField(default=0, verbose_name='Area (Square KM)')),
                ('population', models.PositiveIntegerField(default=0, verbose_name='Population')),
                ('elevation', models.IntegerField(default=0, verbose_name='Elevation')),
                ('geoname_id', models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True)),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('code', models.CharField(blank=True, max_length=40, null=True, verbose_name='Code')),
                ('fips', models.CharField(blank=True, max_length=40, null=True, verbose_name='FIPS')),
                ('altnames', models.ManyToManyField(blank=True, related_name='geoware_subdivision_altnames', to='geoware.Altname', verbose_name='Altname')),
                ('capital', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_subdivision_capital', to='geoware.City', verbose_name='Capital')),
                ('division', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_subdivision_country', to='geoware.Division', verbose_name='Division')),
            ],
            options={
                'verbose_name_plural': 'Subdivisions',
                'verbose_name': 'Subdivision',
                'db_table': 'geoware-subdivision',
            },
        ),
        migrations.CreateModel(
            name='Timezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name_id', models.CharField(db_index=True, max_length=254, verbose_name='Name')),
                ('slug', models.CharField(blank=True, max_length=254, null=True, verbose_name='Slug')),
                ('gmt_offset', models.FloatField(default=0.0, verbose_name='GMT Offset (Jan 1)')),
                ('dst_offset', models.FloatField(default=0.0, verbose_name='DST Offset (Jul 1)')),
                ('raw_offset', models.FloatField(default=0.0, verbose_name='Raw Offset')),
                ('url', models.URLField(blank=True, max_length=254, null=True, verbose_name='URL')),
                ('info', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_timezone_country', to='geoware.Country', verbose_name='Country')),
            ],
            options={
                'verbose_name_plural': 'Timezones',
                'verbose_name': 'Timezone',
                'db_table': 'geoware-timezone',
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
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_currency', to='geoware.Currency', verbose_name='Currency'),
        ),
        migrations.AddField(
            model_name='country',
            name='jurisdiction',
            field=models.ForeignKey(blank=True, help_text='Sovereignty', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_country_jurisdiction', to='geoware.Country', verbose_name='Jurisdiction'),
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(blank=True, related_name='geoware_country_languagues', to='geoware.Language', verbose_name='Languages'),
        ),
        migrations.AddField(
            model_name='country',
            name='neighbors',
            field=models.ManyToManyField(blank=True, related_name='_country_neighbors_+', to='geoware.Country', verbose_name='Neighbors'),
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_country', to='geoware.Country', verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='city',
            name='district_of',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='geoware.City', verbose_name='District Of'),
        ),
        migrations.AddField(
            model_name='city',
            name='division',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_division', to='geoware.Division', verbose_name='Division'),
        ),
        migrations.AddField(
            model_name='city',
            name='subdivision',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_subdivision', to='geoware.Subdivision', verbose_name='Subdivision'),
        ),
        migrations.AddField(
            model_name='city',
            name='timezone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_city_timezone', to='geoware.Timezone', verbose_name='Timezone'),
        ),
        migrations.AddField(
            model_name='altname',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='geoware_altname_language', to='geoware.Language', verbose_name='Language'),
        ),
        migrations.AlterUniqueTogether(
            name='timezone',
            unique_together=set([('name_id',)]),
        ),
        migrations.AlterUniqueTogether(
            name='subdivision',
            unique_together=set([('name', 'fips', 'division')]),
        ),
        migrations.AlterUniqueTogether(
            name='ocean',
            unique_together=set([('name',)]),
        ),
        migrations.AlterUniqueTogether(
            name='division',
            unique_together=set([('fips', 'name_std', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='country',
            unique_together=set([('code',)]),
        ),
        migrations.AlterUniqueTogether(
            name='continent',
            unique_together=set([('name', 'code')]),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'division', 'country')]),
        ),
        migrations.AlterUniqueTogether(
            name='altname',
            unique_together=set([('geoname_id',)]),
        ),
    ]
