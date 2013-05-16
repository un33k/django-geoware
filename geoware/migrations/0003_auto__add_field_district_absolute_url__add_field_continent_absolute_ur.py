# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'District.absolute_url'
        db.add_column('geoware-district', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Continent.absolute_url'
        db.add_column('geoware-continent', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Region.absolute_url'
        db.add_column('geoware-region', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'City.absolute_url'
        db.add_column('geoware-city', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Ocean.absolute_url'
        db.add_column('geoware-ocean', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Subregion.absolute_url'
        db.add_column('geoware-subregion', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Country.absolute_url'
        db.add_column('geoware-country', 'absolute_url',
                      self.gf('django.db.models.fields.CharField')(max_length=254, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'District.absolute_url'
        db.delete_column('geoware-district', 'absolute_url')

        # Deleting field 'Continent.absolute_url'
        db.delete_column('geoware-continent', 'absolute_url')

        # Deleting field 'Region.absolute_url'
        db.delete_column('geoware-region', 'absolute_url')

        # Deleting field 'City.absolute_url'
        db.delete_column('geoware-city', 'absolute_url')

        # Deleting field 'Ocean.absolute_url'
        db.delete_column('geoware-ocean', 'absolute_url')

        # Deleting field 'Subregion.absolute_url'
        db.delete_column('geoware-subregion', 'absolute_url')

        # Deleting field 'Country.absolute_url'
        db.delete_column('geoware-country', 'absolute_url')


    models = {
        'geoware.altname': {
            'Meta': {'object_name': 'Altname', 'db_table': "'geoware-altname'"},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_preferred': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_short': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'language': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_altname_language'", 'null': 'True', 'to': "orm['geoware.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'ref_geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'geoware.city': {
            'Meta': {'object_name': 'City', 'db_table': "'geoware-city'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_city_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bbe': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbn': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbs': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbw': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_country'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'"}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_region'", 'null': 'True', 'to': "orm['geoware.Region']"}),
            'sister': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['geoware.City']", 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'subregion': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_subregion'", 'null': 'True', 'to': "orm['geoware.Subregion']"}),
            'timezone': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_city_timezone'", 'null': 'True', 'to': "orm['geoware.Timezone']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.continent': {
            'Meta': {'unique_together': "[('name', 'code')]", 'object_name': 'Continent', 'db_table': "'geoware-continent'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_continent_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.country': {
            'Meta': {'object_name': 'Country', 'db_table': "'geoware-country'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_country_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_capital'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '2', 'db_index': 'True'}),
            'continent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_continent'", 'null': 'True', 'to': "orm['geoware.Continent']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_currency'", 'null': 'True', 'to': "orm['geoware.Currency']"}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idc': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'iso_3': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'iso_n': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'jurisdiction': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_country_jurisdiction'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'languages': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_country_languagues'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Language']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'neighbours': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'neighbours_rel_+'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'tld': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.currency': {
            'Meta': {'unique_together': "(('name', 'code'),)", 'object_name': 'Currency', 'db_table': "'geoware-currency'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'fractional_ratio': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fractional_unit': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'symbol': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.district': {
            'Meta': {'unique_together': "[('name', 'city')]", 'object_name': 'District', 'db_table': "'geoware-district'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_district_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'bbe': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbn': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbs': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'bbw': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'city': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_district_city'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'point': ('django.contrib.gis.db.models.fields.PointField', [], {'default': "'POINT(0.0 0.0)'"}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.language': {
            'Meta': {'object_name': 'Language', 'db_table': "'geoware-language'"},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'db_index': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dialect': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'percent': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.ocean': {
            'Meta': {'object_name': 'Ocean', 'db_table': "'geoware-ocean'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_ocean_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'depth': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'depth_name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.region': {
            'Meta': {'unique_together': "[('name', 'country')]", 'object_name': 'Region', 'db_table': "'geoware-region'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_region_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_region_capital'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_region_country'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.subregion': {
            'Meta': {'unique_together': "[('name', 'region')]", 'object_name': 'Subregion', 'db_table': "'geoware-subregion'"},
            'absolute_url': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'altnames': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'geoware_subregion_altnames'", 'null': 'True', 'symmetrical': 'False', 'to': "orm['geoware.Altname']"}),
            'area': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'capital': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_subregion_capital'", 'null': 'True', 'to': "orm['geoware.City']"}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'elevation': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'fips': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'geoname_id': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'name_std': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'population': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'region': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_subregion_region'", 'null': 'True', 'to': "orm['geoware.Region']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        },
        'geoware.timezone': {
            'Meta': {'object_name': 'Timezone', 'db_table': "'geoware-timezone'"},
            'country': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'geoware_timezone_country'", 'null': 'True', 'to': "orm['geoware.Country']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'dst_offset': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'gmt_offset': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'info': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name_id': ('django.db.models.fields.CharField', [], {'max_length': '254', 'db_index': 'True'}),
            'raw_offset': ('django.db.models.fields.FloatField', [], {'default': '0.0'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '254', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['geoware']