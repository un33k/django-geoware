from django import template
from django.conf import settings
from ..utils.geoip import get_geoip_info_api_or_cache

register = template.Library()

@register.filter
def geo_country_name(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['country_name'])

@register.filter
def geo_country_code(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['country_code'])

@register.filter
def geo_country_code3(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['country_code3'])

@register.filter
def geo_city(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['city'])

@register.filter
def geo_latitude(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['latitude'])

@register.filter
def geo_longitude(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['longitude'])

@register.filter
def geo_postal_code(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['postal_code'])

@register.filter
def geo_region(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['region'])

@register.filter
def geo_dma_code(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['dma_code'])

@register.filter
def geo_area_code(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['area_code'])

@register.filter
def geo_fqdn_or_ip(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['fqdn_or_ip'])

@register.filter
def geo_charset(request):
    geo_params = get_geoip_info_api_or_cache(request)
    return(geo_params['charset'])


