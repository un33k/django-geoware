import logging
from django.utils.translation import ugettext as _
from django.core.exceptions import ObjectDoesNotExist

from .. import defaults
from ..models import *

logger = logging.getLogger("geoware.utils.fixer")


def get_canadian_provice_code(code_num):
    """ Given a numeric canadian province, returns a alpha version """
    code_alph = None
    try:
        code_alph = defaults.GEOWARE_CANADA_PROVINCE_CODES[code_num]
    except:
        pass
    return code_alph


def region_pre_save_call(region):
    """ Given a region object, this performs any last minutes fixes """

    ## FIX for Canadian Provice Codes
    if 'ca' in region.fips.split('.')[0].lower():
        code = get_canadian_provice_code(region.code)
        if code:
            region.code = code


def subregion_pre_save_call(region):
    """ Given a subregion object, this performs any last minutes fixes """
    pass


def city_pre_save_call(region):
    """ Given a city object, this performs any last minutes fixes """
    pass

def district_pre_save_call(region):
    """ Given a district object, this performs any last minutes fixes """
    pass


def fix_timezone_pre_save(timezone):
    """ Given a timezone object, this performs any last minutes fixes """
    pass

def fix_altname_pre_save(altname):
    """ Given an altname object, this performs any last minutes fixes """
    pass


