from django.conf import settings
from utils.geoip import get_geoip_info_api_or_cache

class GeowareSessionMiddleware(object):

    def process_request(self, request):
        """ Save or update geo info in session """

        get_geoip_info_api_or_cache(request)
        return None


