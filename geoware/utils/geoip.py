import re
from django.conf import settings
from django.contrib.gis.geoip import GeoIP

from toolware.utils.generic import get_encoded_url_to_dict, get_dict_to_encoded_url
from ipware.ip import get_ip_address_from_request

from .. import defaults

def get_fqdn_or_ip(request):
    fqdn_or_ip = getattr(defaults, 'GEOWARE_GEOIP_DEBUG_DOMAIN_OR_IP', None)
    if not fqdn_or_ip:
        fqdn_or_ip = get_ip_address_from_request(request)
    return fqdn_or_ip

def get_geoip_info(request):
    """ Returns geoIP from C API  """

    geoip_info = {
        'fqdn_or_ip': '',
        'city': '', 
        'continent_code': '', 
        'region': '',
        'charset': 0,
        'area_code': 0,
        'longitude': 0.0,
        'country_code3': '',
        'latitude': 0.0,
        'postal_code': None,
        'dma_code': 0,
        'country_code': '',
        'country_name': '',
    }
    fqdn_or_ip = get_fqdn_or_ip(request)
    if fqdn_or_ip:
        geoip = GeoIP(cache=defaults.GEOWARE_GEOIP_CACHE_METHOD)
        try:
            ginfo = geoip.city(fqdn_or_ip)
            geoip_info.update(ginfo)
        except:
            try:
                ginfo = geoip.country(fqdn_or_ip)
                geoip_info.update(ginfo)
            except:
                pass
        geoip_info['fqdn_or_ip'] = fqdn_or_ip
    return geoip_info

def get_geoip_info_api_or_cache(request):
    """ Returns geoIP from session, if not then from C API """

    fqdn_or_ip = get_fqdn_or_ip(request)
    geoip_info = request.session.get('geoip_info', '')
    if geoip_info:
        geo_params = get_encoded_url_to_dict(geoip_info)
        try:
            if geo_params['fqdn_or_ip'] == fqdn_or_ip:
                return geo_params # no change
        except: pass
    geo_params = get_geoip_info(request)
    request.session['geoip_info'] = get_dict_to_encoded_url(geo_params)
    request.session.modified = True
    return geo_params




