# -- coding: utf-8 --

import os
from django.conf import settings
from django.utils.translation import gettext as _
from django.core.exceptions import ImproperlyConfigured
from django.contrib.gis.utils import GeoIP

try:
    from uuslug import slugify
except:
    from django.template.defaultfilters import slugify

GEOWARE_USING_GEO_DJANGO = getattr(settings, 'GEOWARE_USING_GEO_DJANGO', False)

GEOWARE_INCLUDE_TEMPLATE_TAGS = getattr(settings, 'GEOWARE_INCLUDE_TEMPLATE_TAGS', True)
GEOWARE_GEOIP_DEBUG_DOMAIN_OR_IP = getattr(settings, 'GEOWARE_GEOIP_DEBUG_DOMAIN_OR_IP', None)
GEOWARE_GEOIP_CACHE_METHOD = getattr(settings, "GEOWARE_GEOIP_CACHE_METHOD", GeoIP.GEOIP_STANDARD | GeoIP.GEOIP_CHECK_CACHE)

GEOWARE_DATA_DIR = getattr(settings, 'GEOWARE_DATA_DIR',
                os.path.normpath(os.path.join(os.path.expanduser("~"), '.geoware_cache_dir')))


# http://download.geonames.org/export/dump/
# - Countries:            countryInfo.txt
# - Regions:              admin1CodesASCII.txt
# - Subregions:           admin2Codes.txt
# - Cities:               cities5000.zip
# - Timezones:            timeZones.txt
# - Districts:            hierarchy.zip
# - Localization:         alternateNames.zip
# http://download.geonames.org/export/zip/
# - Postal Codes:         allCountries.zip

GEOWARE_BASE_URLS = {
    'geonames': {
        'dump': 'http://download.geonames.org/export/dump/',
        'zip': 'http://download.geonames.org/export/zip/',
    },
    'maxmind': {
        'GeoIP.dat': 'http://geolite.maxmind.com/download/geoip/database/GeoLiteCountry/GeoIP.dat.gz',
        'GeoLiteCity.dat': 'http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz',
        'GeoIPv6.dat': 'http://geolite.maxmind.com/download/geoip/database/GeoIPv6.dat.gz',
        'GeoLiteCityv6.dat': 'http://geolite.maxmind.com/download/geoip/database/GeoLiteCityv6-beta/GeoLiteCityv6.dat.gz',
    },    
}

GEOWARE_CITY_FILE_POPULATION_MIN = getattr(settings, 'GEOWARE_CITY_FILE_POPULATION_MIN', 1000)
if GEOWARE_CITY_FILE_POPULATION_MIN not in [1000, 5000, 15000]:
    GEOWARE_CITY_FILE_POPULATION_MIN = 15000

GEOWARE_FILE_DICT = {
    'country':      {
        'filename': 'countryInfo.txt',
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'region':       {
        'filename': 'admin1CodesASCII.txt',
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'subregion':    {
        'filename': 'admin2Codes.txt',
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'city':         {
        'filename': 'cities{0}.zip'.format(GEOWARE_CITY_FILE_POPULATION_MIN),
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'timezone':     {
        'filename': 'timeZones.txt',
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'district':    {
        'filename': 'hierarchy.zip',
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'altname':     {
        'filename': 'alternateNames.zip',
        'url':     GEOWARE_BASE_URLS['geonames']['dump']+'{filename}'
    },
    'postalcode':  {
        'filename': 'allCountries.zip',
        'url':     GEOWARE_BASE_URLS['geonames']['zip']+'{filename}'
    }
}


GEOWARE_COUNTRY_CODES = [
    'AD','AE','AF','AG','AI','AL','AM','AO','AQ','AR','AS','AT','AU','AW','AX','AZ',
    'BA','BB','BD','BE','BF','BG','BH','BI','BJ','BL','BM','BN','BO','BQ','BR','BS','BT','BV','BW','BY','BZ',
    'CA','CC','CD','CF','CG','CH','CI','CK','CL','CM','CN','CO','CR','CU','CV','CW','CX','CY','CZ',
    'DE','DJ','DK','DM','DO','DZ','EC','EE','EG','EH','ER','ES','ET','FI','FJ','FK','FM','FO','FR',
    'GA','GB','GD','GE','GF','GG','GH','GI','GL','GM','GN','GP','GQ','GR','GS','GT','GU','GW','GY',
    'HK','HM','HN','HR','HT','HU','ID','IE','IL','IM','IN','IO','IQ','IR','IS','IT','JE','JM','JO','JP',
    'KE','KG','KH','KI','KM','KN','KP','KR','XK','KW','KY','KZ','LA','LB','LC','LI','LK','LR','LS','LT','LU','LV','LY',
    'MA','MC','MD','ME','MF','MG','MH','MK','ML','MM','MN','MO','MP','MQ','MR','MS','MT','MU','MV','MW','MX','MY','MZ',
    'NA','NC','NE','NF','NG','NI','NL','NO','NP','NR','NU','NZ','OM',
    'PA','PE','PF','PG','PH','PK','PL','PM','PN','PR','PS','PT','PW','PY','QA','RE','RO','RS','RU','RW',
    'SA','SB','SC','SD','SS','SE','SG','SH','SI','SJ','SK','SL','SM','SN','SO','SR','ST','SV','SX','SY','SZ',
    'TC','TD','TF','TG','TH','TJ','TK','TL','TM','TN','TO','TR','TT','TV','TW','TZ','UA','UG','UM','US','UY','UZ',
    'VA','VC','VE','VG','VI','VN','VU','WF','WS','YE','YT','ZA','ZM','ZW',
]

# See http://www.geonames.org/export/codes.html
GEOWARE_CITY_TYPES = ['PPL','PPLA','PPLC','PPLA2','PPLA3','PPLA4', 'PPLG']
GEOWARE_DISTRICT_TYPES = ['PPLX']
GEOWARE_CAPITAL_TYPES = ['PPLC']

GEOWARE_LOADING_ORDER = [
    'Country',
    'Timezone',
    'Region',
    'Subregion',
    'City',
    'District',
]

GEOWARE_CONTINENT_CHOICES = (
    ('OC', _(u'Oceania')),
    ('EU', _(u'Europe')),
    ('AF', _(u'Africa')),
    ('NA', _(u'North America')),
    ('AN', _(u'Antarctica')),
    ('SA', _(u'South America')),
    ('AS', _(u'Asia')),
)

GEOWARE_OCEAN_CHOICES = (
    ('Arctic', _(u'Arctic')),
    ('Atlantic', _(u'Atlantic')),
    ('Indian', _(u'Indian')),
    ('Pacific', _(u'Pacific')),
    ('Southern', _(u'Southern')),
)

GEOWARE_CANADA_PROVINCE_CODES = {
    '01': 'AB',
    '02': 'BC',
    '03': 'MB',
    '04': 'NB',
    '05': 'NL',
    '07': 'NS',
    '08': 'ON',
    '09': 'PE',
    '10': 'QC',
    '11': 'SK',
    '12': 'YT',
    '13': 'NT',
    '14': 'NU',
}

GEOWARE_LANGUAGE_CHOICES = (
    ('af',      _(u'Afrikaans')),
    ('af-ZA',   _(u'Afrikaans (South Africa)')),
    ('ar',      _(u'Arabic')),
    ('ar-AE',   _(u'Arabic (UAE)')),
    ('ar-BH',   _(u'Arabic (Bahrain)')),
    ('ar-DZ',   _(u'Arabic (Algeria)')),
    ('ar-EG',   _(u'Arabic (Egypt)')),
    ('ar-IQ',   _(u'Arabic (Iraq)')),
    ('ar-JO',   _(u'Arabic (Jordan)')),
    ('ar-KW',   _(u'Arabic (Kuwait)')),
    ('ar-LB',   _(u'Arabic (Lebanon)')),
    ('ar-LY',   _(u'Arabic (Libya)')),
    ('ar-MA',   _(u'Arabic (Morocco)')),
    ('ar-OM',   _(u'Arabic (Oman)')),
    ('ar-QA',   _(u'Arabic (Qatar)')),
    ('ar-SA',   _(u'Arabic (Saudi Arabia)')),
    ('ar-SY',   _(u'Arabic (Syria)')),
    ('ar-TN',   _(u'Arabic (Tunisia)')),
    ('ar-YE',   _(u'Arabic (Yemen)')),
    ('az',      _(u'Azeri')),
    ('az-AZ',   _(u'Azeri (Azerbaijan)')),
    ('be',      _(u'Belarusian')),
    ('be-BY',   _(u'Belarusian (Belarus)')),
    ('bg',      _(u'Bulgarian')),
    ('bg-BG',   _(u'Bulgarian (Bulgaria)')),
    ('bs-BA',   _(u'Bosnian (Bosnia and Herzegovina)')),
    ('ca',      _(u'Catalan')),
    ('ca-ES',   _(u'Catalan (Spain)')),
    ('cs',      _(u'Czech')),
    ('cs-CZ',   _(u'Czech (Czech Republic)')),
    ('cy',      _(u'Welsh')),
    ('cy-GB',   _(u'Welsh (United Kingdom)')),
    ('da',      _(u'Danish')),
    ('da-DK',   _(u'Danish (Denmark)')),
    ('de',      _(u'German')),
    ('de-AT',   _(u'German (Austria)')),
    ('de-CH',   _(u'German (Switzerland)')),
    ('de-DE',   _(u'German (Germany)')),
    ('de-LI',   _(u'German (Liechtenstein)')),
    ('de-LU',   _(u'German (Luxembourg)')),
    ('dv',      _(u'Divehi')),
    ('dv-MV',   _(u'Divehi (Maldives)')),
    ('el',      _(u'Greek')),
    ('el-GR',   _(u'Greek (Greece)')),
    ('en',      _(u'English')),
    ('en-AU',   _(u'English (Australia)')),
    ('en-BZ',   _(u'English (Belize)')),
    ('en-CA',   _(u'English (Canada)')),
    ('en-CB',   _(u'English (Caribbean)')),
    ('en-GB',   _(u'English (United Kingdom)')),
    ('en-IE',   _(u'English (Ireland)')),
    ('en-JM',   _(u'English (Jamaica)')),
    ('en-NZ',   _(u'English (New Zealand)')),
    ('en-PH',   _(u'English (The Philippines)')),
    ('en-TT',   _(u'English (Trinidad and Tobago)')),
    ('en-US',   _(u'English (United States)')),
    ('en-VC',   _(u'English (Saint Vincent and the Grenadines)')),
    ('en-VG',   _(u'English (British Virgin Islands)')),
    ('en-ZA',   _(u'English (South Africa)')),
    ('en-ZW',   _(u'English (Zimbabwe)')),
    ('eo',      _(u'Esperanto')),
    ('es',      _(u'Spanish')),
    ('es-AR',   _(u'Spanish (Argentina)')),
    ('es-BO',   _(u'Spanish (Bolivia)')),
    ('es-CL',   _(u'Spanish (Chile)')),
    ('es-CO',   _(u'Spanish (Colombia)')),
    ('es-CR',   _(u'Spanish (Costa Rica)')),
    ('es-DO',   _(u'Spanish (Dominican Republic)')),
    ('es-EC',   _(u'Spanish (Ecuador)')),
    ('es-ES',   _(u'Spanish (Castilian)')),
    ('es-ES',   _(u'Spanish (Spain)')),
    ('es-GT',   _(u'Spanish (Guatemala)')),
    ('es-HN',   _(u'Spanish (Honduras)')),
    ('es-MX',   _(u'Spanish (Mexico)')),
    ('es-NI',   _(u'Spanish (Nicaragua)')),
    ('es-PA',   _(u'Spanish (Panama)')),
    ('es-PE',   _(u'Spanish (Peru)')),
    ('es-PR',   _(u'Spanish (Puerto Rico)')),
    ('es-PY',   _(u'Spanish (Paraguay)')),
    ('es-SV',   _(u'Spanish (El Salvador)')),
    ('es-UY',   _(u'Spanish (Uruguay)')),
    ('es-VE',   _(u'Spanish (Venezuela)')),
    ('et',      _(u'Estonian')),
    ('et-EE',   _(u'Estonian (Estonia)')),
    ('eu',      _(u'Basque')),
    ('eu-ES',   _(u'Basque (Spain)')),
    ('fa',      _(u'Farsi')),
    ('fa-IR',   _(u'Farsi (Iran)')),
    ('fi',      _(u'Finnish')),
    ('fi-FI',   _(u'Finnish (Finland)')),
    ('fo',      _(u'Faroese')),
    ('fo-FO',   _(u'Faroese (Faroe Islands)')),
    ('fr',      _(u'French')),
    ('fr-BE',   _(u'French (Belgium)')),
    ('fr-CA',   _(u'French (Canada)')),
    ('fr-CH',   _(u'French (Switzerland)')),
    ('fr-FR',   _(u'French (France)')),
    ('fr-LU',   _(u'French (Luxembourg)')),
    ('fr-MC',   _(u'French (Monaco)')),
    ('fr-WF',   _(u'French (Futuna)')),
    ('fud',     _(u'Futunian (Futuna)')),
    ('gl',      _(u'Galician')),
    ('gl-ES',   _(u'Galician (Spain)')),
    ('gu',      _(u'Gujarati')),
    ('gu-IN',   _(u'Gujarati (India)')),
    ('he',      _(u'Hebrew')),
    ('he-IL',   _(u'Hebrew (Israel)')),
    ('hi',      _(u'Hindi')),
    ('hi-IN',   _(u'Hindi (India)')),
    ('hr',      _(u'Croatian')),
    ('hr-BA',   _(u'Croatian (Bosnia and Herzegovina)')),
    ('hr-HR',   _(u'Croatian (Croatia)')),
    ('hu',      _(u'Hungarian')),
    ('hu-HU',   _(u'Hungarian (Hungary)')),
    ('hy',      _(u'Armenian')),
    ('hy-AM',   _(u'Armenian (Armenia)')),
    ('id',      _(u'Indonesian')),
    ('id-ID',   _(u'Indonesian (Indonesia)')),
    ('is',      _(u'Icelandic')),
    ('is-IS',   _(u'Icelandic (Iceland)')),
    ('it',      _(u'Italian')),
    ('it-CH',   _(u'Italian (Switzerland)')),
    ('it-IT',   _(u'Italian (Italy)')),
    ('ja',      _(u'Japanese')),
    ('ja-JP',   _(u'Japanese (Japan)')),
    ('ka',      _(u'Georgian')),
    ('ka-GE',   _(u'Georgian (Georgia)')),
    ('kk',      _(u'Kazakh')),
    ('kk-KZ',   _(u'Kazakh (Kazakhstan)')),
    ('kn',      _(u'Kannada')),
    ('kn-IN',   _(u'Kannada (India)')),
    ('ko',      _(u'Korean')),
    ('ko-KR',   _(u'Korean (Korea)')),
    ('kok',     _(u'Konkani')),
    ('kok-IN',  _(u'Konkani (India)')),
    ('ky',      _(u'Kyrgyz')),
    ('ky-KG',   _(u'Kyrgyz (Kyrgyzstan)')),
    ('lt',      _(u'Lithuanian')),
    ('lt-LT',   _(u'Lithuanian (Lithuania)')),
    ('lv',      _(u'Latvian')),
    ('lv-LV',   _(u'Latvian (Latvia)')),
    ('mi',      _(u'Maori')),
    ('mi-NZ',   _(u'Maori (New Zealand)')),
    ('mk',      _(u'Macedonian')),
    ('mk-MK',   _(u'Macedonian (Republic of Macedonia)')),
    ('mn',      _(u'Mongolian')),
    ('mn-MN',   _(u'Mongolian (Mongolia)')),
    ('mr',      _(u'Marathi')),
    ('mr-IN',   _(u'Marathi (India)')),
    ('ms',      _(u'Malay')),
    ('ms-BN',   _(u'Malay (Brunei Darussalam)')),
    ('ms-MY',   _(u'Malay (Malaysia)')),
    ('mt',      _(u'Maltese')),
    ('mt-MT',   _(u'Maltese (Malta)')),
    ('nb',      _(u'Norwegian Bokmal')),
    ('nb-NO',   _(u'Norwegian Bokmal (Norway)')),
    ('nl',      _(u'Dutch')),
    ('nl-BE',   _(u'Dutch (Belgium)')),
    ('nl-NL',   _(u'Dutch (Netherlands)')),
    ('nn-NO',   _(u'Norwegian Nynorsk (Norway)')),
    ('ns',      _(u'Northern Sotho')),
    ('ns-ZA',   _(u'Northern Sotho (South Africa)')),
    ('pa',      _(u'Punjabi')),
    ('pa-IN',   _(u'Punjabi (India)')),
    ('pl',      _(u'Polish')),
    ('pl-PL',   _(u'Polish (Poland)')),
    ('ps',      _(u'Pashto')),
    ('ps-AR',   _(u'Pashto (Afghanistan)')),
    ('pt',      _(u'Portuguese')),
    ('pt-BR',   _(u'Portuguese (Brazil)')),
    ('pt-PT',   _(u'Portuguese (Portugal)')),
    ('qu',      _(u'Quechua')),
    ('qu-BO',   _(u'Quechua (Bolivia)')),
    ('qu-EC',   _(u'Quechua (Ecuador)')),
    ('qu-PE',   _(u'Quechua (Peru)')),
    ('ro',      _(u'Romanian')),
    ('ro-RO',   _(u'Romanian (Romania)')),
    ('ru',      _(u'Russian')),
    ('ru-RU',   _(u'Russian (Russia)')),
    ('sa',      _(u'Sanskrit')),
    ('sa-IN',   _(u'Sanskrit (India)')),
    ('se',      _(u'Sami (Northern)')),
    ('se-FI',   _(u'Sami (Finland)')),
    ('se-NO',   _(u'Sami (Norway)')),
    ('se-SE',   _(u'Sami (Sweden)')),
    ('sk',      _(u'Slovak')),
    ('sk-SK',   _(u'Slovak (Slovakia)')),
    ('sl',      _(u'Slovenian')),
    ('sl-SI',   _(u'Slovenian (Slovenia)')),
    ('sq',      _(u'Albanian')),
    ('sq-AL',   _(u'Albanian (Albania)')),
    ('sr-BA',   _(u'Serbian (Bosnia and Herzegovina)')),
    ('sr-SP',   _(u'Serbian (Serbia and Montenegro)')),
    ('sv',      _(u'Swedish')),
    ('sv-FI',   _(u'Swedish (Finland)')),
    ('sv-SE',   _(u'Swedish (Sweden)')),
    ('sw',      _(u'Swahili')),
    ('sw-KE',   _(u'Swahili (Kenya)')),
    ('syr',     _(u'Syriac')),
    ('syr-SY',  _(u'Syriac (Syria)')),
    ('ta',      _(u'Tamil')),
    ('ta-IN',   _(u'Tamil (India)')),
    ('te',      _(u'Telugu')),
    ('te-IN',   _(u'Telugu (India)')),
    ('th',      _(u'Thai')),
    ('th-TH',   _(u'Thai (Thailand)')),
    ('tl',      _(u'Tagalog')),
    ('tl-PH',   _(u'Tagalog (The Philippines)')),
    ('tn',      _(u'Tswana')),
    ('tn-ZA',   _(u'Tswana (South Africa)')),
    ('tr',      _(u'Turkish')),
    ('tr-TR',   _(u'Turkish (Turkey)')),
    ('tt',      _(u'Tatar')),
    ('tt-RU',   _(u'Tatar (Russia)')),
    ('ts',      _(u'Tsonga')),
    ('uk',      _(u'Ukrainian')),
    ('uk-UA',   _(u'Ukrainian (Ukraine)')),
    ('ur',      _(u'Urdu')),
    ('ur-PK',   _(u'Urdu (Pakistan)')),
    ('uz',      _(u'Uzbek (Latin)')),
    ('uz-UZ',   _(u'Uzbek (Uzbekistan)')),
    ('vi',      _(u'Vietnamese')),
    ('vi-VN',   _(u'Vietnamese (Viet Nam)')),
    ('wls',     _(u'Wallisian (Noumea)')),
    ('xh',      _(u'Xhosa')),
    ('xh-ZA',   _(u'Xhosa (South Africa)')),
    ('zh',      _(u'Chinese')),
    ('zh-CN',   _(u'Chinese (Simplified)')),
    ('zh-HK',   _(u'Chinese (Hong Kong)')),
    ('zh-MO',   _(u'Chinese (Macau)')),
    ('zh-SG',   _(u'Chinese (Singapore)')),
    ('zh-TW',   _(u'Chinese (Traditional)')),
    ('zu',      _(u'Zulu')),
    ('zu-ZA',   _(u'Zulu (South Africa)')),
)

GEOWARE_CURRENCY_CHOICES = {
  "AED": {
    "code": "AED",
    "fractional_ratio": "100",
    "fractional_unit": "Fils",
    "name": "Dirham (United Arab Emirates)",
    "symbol": "د.إ"
  },
  "AFN": {
    "code": "AFN",
    "fractional_ratio": "100",
    "fractional_unit": "Pul",
    "name": "Afghani (Afghanistan)",
    "symbol": "؋"
  },
  "ALL": {
    "code": "ALL",
    "fractional_ratio": "100",
    "fractional_unit": "Qindarkë",
    "name": "Lek (Albania)",
    "symbol": "L"
  },
  "AMD": {
    "code": "AMD",
    "fractional_ratio": "100",
    "fractional_unit": "Luma",
    "name": "Dram (Armenia)",
    "symbol": "դր."
  },
  "ANG": {
    "code": "ANG",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Antilles Guilder (Netherlands)",
    "symbol": "ƒ"
  },
  "AOA": {
    "code": "AOA",
    "fractional_ratio": "100",
    "fractional_unit": "Cêntimo",
    "name": "Kwanza (Angola)",
    "symbol": "Kz"
  },
  "AQD": {
    "code": "AQD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Antarctica)",
    "symbol": "$"
  },
  "ARS": {
    "code": "ARS",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Peso (Argentina)",
    "symbol": "$"
  },
  "AUD": {
    "code": "AUD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Australia)",
    "symbol": "$"
  },
  "AWG": {
    "code": "AWG",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Guilder (Aruba)",
    "symbol": "ƒ"
  },
  "AZN": {
    "code": "AZN",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "New Manat (Azerbaijan)",
    "symbol": ""
  },
  "BAM": {
    "code": "BAM",
    "fractional_ratio": "100",
    "fractional_unit": "Fening",
    "name": "Convertible Marka (Bosnia and Herzegovina)",
    "symbol": "KM or КМ"
  },
  "BBD": {
    "code": "BBD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Barbados)",
    "symbol": "$"
  },
  "BDT": {
    "code": "BDT",
    "fractional_ratio": "100",
    "fractional_unit": "Paisa",
    "name": "Taka (Bangladesh)",
    "symbol": "৳"
  },
  "BGN": {
    "code": "BGN",
    "fractional_ratio": "100",
    "fractional_unit": "Stotinka",
    "name": "Lev (Bulgaria)",
    "symbol": "лв"
  },
  "BHD": {
    "code": "BHD",
    "fractional_ratio": "1000",
    "fractional_unit": "Fils",
    "name": "Dinar (Bahrain)",
    "symbol": ".د.ب"
  },
  "BIF": {
    "code": "BIF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Burundi)",
    "symbol": "Fr"
  },
  "BMD": {
    "code": "BMD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Bermuda)",
    "symbol": "$"
  },
  "BND": {
    "code": "BND",
    "fractional_ratio": "100",
    "fractional_unit": "Sen",
    "name": "Darussalam Dollar (Brunei)",
    "symbol": "$"
  },
  "BOB": {
    "code": "BOB",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Boliviano (Bolivia)",
    "symbol": "Bs."
  },
  "BRL": {
    "code": "BRL",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Real (Brazil)",
    "symbol": "R$"
  },
  "BSD": {
    "code": "BSD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Bahamas)",
    "symbol": "$"
  },
  "BTN": {
    "code": "BTN",
    "fractional_ratio": "100",
    "fractional_unit": "Chetrum",
    "name": "Ngultrum (Bhutan)",
    "symbol": "Nu."
  },
  "BWP": {
    "code": "BWP",
    "fractional_ratio": "100",
    "fractional_unit": "Thebe",
    "name": "Pula (Botswana)",
    "symbol": "P"
  },
  "BYR": {
    "code": "BYR",
    "fractional_ratio": "100",
    "fractional_unit": "Kapyeyka",
    "name": "Ruble (Belarus)",
    "symbol": "Br"
  },
  "BZD": {
    "code": "BZD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Belize)",
    "symbol": "$"
  },
  "CAD": {
    "code": "CAD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Canada)",
    "symbol": "$"
  },
  "CDF": {
    "code": "CDF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Congo/Kinshasa)",
    "symbol": "Fr"
  },
  "CHF": {
    "code": "CHF",
    "fractional_ratio": "100",
    "fractional_unit": "Rappen",
    "name": "Franc (Switzerland)",
    "symbol": "Fr"
  },
  "CLP": {
    "code": "CLP",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Peso (Chile)",
    "symbol": "$"
  },
  "CNY": {
    "code": "CNY",
    "fractional_ratio": "100",
    "fractional_unit": "Fen",
    "name": "Yuan Renminbi (China)",
    "symbol": "¥ or 元"
  },
  "COP": {
    "code": "COP",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Peso (Colombia)",
    "symbol": "$"
  },
  "CRC": {
    "code": "CRC",
    "fractional_ratio": "100",
    "fractional_unit": "Céntimo",
    "name": "Colon (Costa Rica)",
    "symbol": "₡"
  },
  "CUC": {
    "code": "CUC",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Convertible Peso (Cuba)",
    "symbol": "$"
  },
  "CUP": {
    "code": "CUP",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Peso (Cuba)",
    "symbol": ""
  },
  "CVE": {
    "code": "CVE",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Escudo (Cape Verde)",
    "symbol": "Esc or $"
  },
  "CZK": {
    "code": "CZK",
    "fractional_ratio": "100",
    "fractional_unit": "Haléř",
    "name": "Koruna (Czech Republic)",
    "symbol": "Kč"
  },
  "DJF": {
    "code": "DJF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Djibouti)",
    "symbol": "Fr"
  },
  "DKK": {
    "code": "DKK",
    "fractional_ratio": "100",
    "fractional_unit": "Øre",
    "name": "Krone (Denmark)",
    "symbol": "kr"
  },
  "DOP": {
    "code": "DOP",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Peso (Dominican Republic)",
    "symbol": "$"
  },
  "DZD": {
    "code": "DZD",
    "fractional_ratio": "100",
    "fractional_unit": "Santeem",
    "name": "Dinar (Algeria)",
    "symbol": "د.ج"
  },
  "EGP": {
    "code": "EGP",
    "fractional_ratio": "100",
    "fractional_unit": "Piastre",
    "name": "Pound (Egypt)",
    "symbol": "£ or ج.م"
  },
  "ERN": {
    "code": "ERN",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Nakfa (Eritrea)",
    "symbol": "Nfk"
  },
  "ETB": {
    "code": "ETB",
    "fractional_ratio": "100",
    "fractional_unit": "Santim",
    "name": "Birr (Ethiopia)",
    "symbol": "Br"
  },
  "EUR": {
    "code": "EUR",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Euro (European Union Countries)",
    "symbol": "€"
  },
  "FJD": {
    "code": "FJD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Fiji)",
    "symbol": "$"
  },
  "FKP": {
    "code": "FKP",
    "fractional_ratio": "100",
    "fractional_unit": "Penny",
    "name": "Malvinas Pound (Falkland Islands)",
    "symbol": "£"
  },
  "GBP": {
    "code": "GBP",
    "fractional_ratio": "100",
    "fractional_unit": "Penny",
    "name": "Pound (United Kingdom)",
    "symbol": "£"
  },
  "GEL": {
    "code": "GEL",
    "fractional_ratio": "100",
    "fractional_unit": "Tetri",
    "name": "Lari (Georgia)",
    "symbol": "ლ"
  },
  "GGP": {
    "code": "GGP",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Pound (Guernsey)",
    "symbol": ""
  },
  "GHS": {
    "code": "GHS",
    "fractional_ratio": "100",
    "fractional_unit": "Pesewa",
    "name": "Cedi (Ghana)",
    "symbol": "₵"
  },
  "GIP": {
    "code": "GIP",
    "fractional_ratio": "100",
    "fractional_unit": "Penny",
    "name": "Pound (Gibraltar)",
    "symbol": "£"
  },
  "GMD": {
    "code": "GMD",
    "fractional_ratio": "100",
    "fractional_unit": "Butut",
    "name": "Dalasi (Gambia)",
    "symbol": "D"
  },
  "GNF": {
    "code": "GNF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Guinea)",
    "symbol": "Fr"
  },
  "GTQ": {
    "code": "GTQ",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Quetzal (Guatemala)",
    "symbol": "Q"
  },
  "GYD": {
    "code": "GYD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Guyana)",
    "symbol": "$"
  },
  "HKD": {
    "code": "HKD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Hong Kong)",
    "symbol": "$"
  },
  "HNL": {
    "code": "HNL",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Lempira (Honduras)",
    "symbol": "L"
  },
  "HRK": {
    "code": "HRK",
    "fractional_ratio": "100",
    "fractional_unit": "Lipa",
    "name": "Kuna (Croatia)",
    "symbol": "kn"
  },
  "HTG": {
    "code": "HTG",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Gourde (Haiti)",
    "symbol": "G"
  },
  "HUF": {
    "code": "HUF",
    "fractional_ratio": "100",
    "fractional_unit": "Fillér",
    "name": "Forint (Hungary)",
    "symbol": "Ft"
  },
  "IDR": {
    "code": "IDR",
    "fractional_ratio": "100",
    "fractional_unit": "Sen",
    "name": "Rupiah (Indonesia)",
    "symbol": "Rp"
  },
  "ILS": {
    "code": "ILS",
    "fractional_ratio": "100",
    "fractional_unit": "Agora",
    "name": "Shekel (Israel)",
    "symbol": "₪"
  },
  "IMP": {
    "code": "IMP",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Pound (Isle of Man)",
    "symbol": ""
  },
  "INR": {
    "code": "INR",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Rupee (India)",
    "symbol": ""
  },
  "IQD": {
    "code": "IQD",
    "fractional_ratio": "1000",
    "fractional_unit": "Fils",
    "name": "Dinar (Iraq)",
    "symbol": "ع.د"
  },
  "IRR": {
    "code": "IRR",
    "fractional_ratio": "1",
    "fractional_unit": "Rial",
    "name": "Rial (Iran)",
    "symbol": "﷼"
  },
  "ISK": {
    "code": "ISK",
    "fractional_ratio": "100",
    "fractional_unit": "Eyrir",
    "name": "Krona (Iceland)",
    "symbol": "kr"
  },
  "JEP": {
    "code": "JEP",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Pound (Jersey)",
    "symbol": ""
  },
  "JMD": {
    "code": "JMD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Jamaica)",
    "symbol": "$"
  },
  "JOD": {
    "code": "JOD",
    "fractional_ratio": "100",
    "fractional_unit": "Piastre",
    "name": "Dinar (Jordan)",
    "symbol": "د.ا"
  },
  "JPY": {
    "code": "JPY",
    "fractional_ratio": "100",
    "fractional_unit": "Sen",
    "name": "Yen (Japan)",
    "symbol": "¥"
  },
  "KES": {
    "code": "KES",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Shilling (Kenya)",
    "symbol": "Sh"
  },
  "KGS": {
    "code": "KGS",
    "fractional_ratio": "100",
    "fractional_unit": "Tyiyn",
    "name": "Som (Kyrgyzstan)",
    "symbol": "лв"
  },
  "KHR": {
    "code": "KHR",
    "fractional_ratio": "100",
    "fractional_unit": "Sen",
    "name": "Riel (Cambodia)",
    "symbol": "៛"
  },
  "KMF": {
    "code": "KMF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Comoros)",
    "symbol": "Fr"
  },
  "KPW": {
    "code": "KPW",
    "fractional_ratio": "100",
    "fractional_unit": "Chon",
    "name": "Won (North Korea)",
    "symbol": "₩"
  },
  "KRW": {
    "code": "KRW",
    "fractional_ratio": "100",
    "fractional_unit": "Jeon",
    "name": "Won (South Korea)",
    "symbol": "₩"
  },
  "KWD": {
    "code": "KWD",
    "fractional_ratio": "1000",
    "fractional_unit": "Fils",
    "name": "Dinar (Kuwait)",
    "symbol": "د.ك"
  },
  "KYD": {
    "code": "KYD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Cayman Islands)",
    "symbol": "$"
  },
  "KZT": {
    "code": "KZT",
    "fractional_ratio": "100",
    "fractional_unit": "Tïın",
    "name": "Tenge (Kazakhstan)",
    "symbol": "₸"
  },
  "LAK": {
    "code": "LAK",
    "fractional_ratio": "100",
    "fractional_unit": "Att",
    "name": "Kip (Laos)",
    "symbol": "₭"
  },
  "LBP": {
    "code": "LBP",
    "fractional_ratio": "100",
    "fractional_unit": "Piastre",
    "name": "Pound (Lebanon)",
    "symbol": "ل.ل"
  },
  "LKR": {
    "code": "LKR",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Rupee (Sri Lanka)",
    "symbol": "Rs"
  },
  "LRD": {
    "code": "LRD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Liberia)",
    "symbol": "$"
  },
  "LSL": {
    "code": "LSL",
    "fractional_ratio": "100",
    "fractional_unit": "Sente",
    "name": "Loti (Lesotho)",
    "symbol": "L"
  },
  "LTL": {
    "code": "LTL",
    "fractional_ratio": "100",
    "fractional_unit": "Centas",
    "name": "Litas (Lithuania)",
    "symbol": "Lt"
  },
  "LVL": {
    "code": "LVL",
    "fractional_ratio": "100",
    "fractional_unit": "Santīms",
    "name": "Lat (Latvia)",
    "symbol": "Ls"
  },
  "LYD": {
    "code": "LYD",
    "fractional_ratio": "1000",
    "fractional_unit": "Dirham",
    "name": "Dinar (Libya)",
    "symbol": "ل.د"
  },
  "MAD": {
    "code": "MAD",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Dirham (Morocco)",
    "symbol": "د.م."
  },
  "MDL": {
    "code": "MDL",
    "fractional_ratio": "100",
    "fractional_unit": "Ban",
    "name": "Leu (Moldova)",
    "symbol": "L"
  },
  "MGA": {
    "code": "MGA",
    "fractional_ratio": "5",
    "fractional_unit": "Iraimbilanja",
    "name": "Ariary (Madagascar)",
    "symbol": "Ar"
  },
  "MKD": {
    "code": "MKD",
    "fractional_ratio": "100",
    "fractional_unit": "Deni",
    "name": "Denar (Macedonia)",
    "symbol": "ден"
  },
  "MMK": {
    "code": "MMK",
    "fractional_ratio": "100",
    "fractional_unit": "Pya",
    "name": "Kyat (Myanmar)",
    "symbol": "Ks"
  },
  "MNT": {
    "code": "MNT",
    "fractional_ratio": "100",
    "fractional_unit": "Möngö",
    "name": "Tughrik (Mongolia)",
    "symbol": "₮"
  },
  "MOP": {
    "code": "MOP",
    "fractional_ratio": "100",
    "fractional_unit": "Avo",
    "name": "Pataca (Macau)",
    "symbol": "P"
  },
  "MRO": {
    "code": "MRO",
    "fractional_ratio": "5",
    "fractional_unit": "Khoums",
    "name": "Ouguiya (Mauritania)",
    "symbol": "UM"
  },
  "MUR": {
    "code": "MUR",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Rupee (Mauritius)",
    "symbol": "₨"
  },
  "MVR": {
    "code": "MVR",
    "fractional_ratio": "100",
    "fractional_unit": "Laari",
    "name": "Rufiyaa (Maldives)",
    "symbol": ".ރ"
  },
  "MWK": {
    "code": "MWK",
    "fractional_ratio": "100",
    "fractional_unit": "Tambala",
    "name": "Kwacha (Malawi)",
    "symbol": "MK"
  },
  "MXN": {
    "code": "MXN",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Peso (Mexico)",
    "symbol": "$"
  },
  "MYR": {
    "code": "MYR",
    "fractional_ratio": "100",
    "fractional_unit": "Sen",
    "name": "Ringgit (Malaysia)",
    "symbol": "RM"
  },
  "MZN": {
    "code": "MZN",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Metical (Mozambique)",
    "symbol": "MT"
  },
  "NAD": {
    "code": "NAD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Namibia)",
    "symbol": "$"
  },
  "NGN": {
    "code": "NGN",
    "fractional_ratio": "100",
    "fractional_unit": "Kobo",
    "name": "Naira (Nigeria)",
    "symbol": "₦"
  },
  "NIO": {
    "code": "NIO",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Cordoba (Nicaragua)",
    "symbol": "C$"
  },
  "NOK": {
    "code": "NOK",
    "fractional_ratio": "100",
    "fractional_unit": "Øre",
    "name": "Krone (Norway)",
    "symbol": "kr"
  },
  "NPR": {
    "code": "NPR",
    "fractional_ratio": "100",
    "fractional_unit": "Paisa",
    "name": "Rupee (Nepal)",
    "symbol": "₨"
  },
  "NZD": {
    "code": "NZD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (New Zealand)",
    "symbol": "$"
  },
  "OMR": {
    "code": "OMR",
    "fractional_ratio": "1000",
    "fractional_unit": "Baisa",
    "name": "Rial (Oman)",
    "symbol": "ر.ع."
  },
  "PAB": {
    "code": "PAB",
    "fractional_ratio": "100",
    "fractional_unit": "Centésimo",
    "name": "Balboa (Panama)",
    "symbol": "B/."
  },
  "PEN": {
    "code": "PEN",
    "fractional_ratio": "100",
    "fractional_unit": "Céntimo",
    "name": "Sol (Peru Nuevo)",
    "symbol": "S/."
  },
  "PGK": {
    "code": "PGK",
    "fractional_ratio": "100",
    "fractional_unit": "Toea",
    "name": "Kina (Papua New Guinea)",
    "symbol": "K"
  },
  "PHP": {
    "code": "PHP",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Peso (Philippines)",
    "symbol": "₱"
  },
  "PKR": {
    "code": "PKR",
    "fractional_ratio": "100",
    "fractional_unit": "Paisa",
    "name": "Rupee (Pakistan)",
    "symbol": "₨"
  },
  "PLN": {
    "code": "PLN",
    "fractional_ratio": "100",
    "fractional_unit": "Grosz",
    "name": "Zloty (Poland)",
    "symbol": "zł"
  },
  "PYG": {
    "code": "PYG",
    "fractional_ratio": "100",
    "fractional_unit": "Céntimo",
    "name": "Guarani (Paraguay)",
    "symbol": "₲"
  },
  "QAR": {
    "code": "QAR",
    "fractional_ratio": "100",
    "fractional_unit": "Dirham",
    "name": "Riyal (Qatar)",
    "symbol": "ر.ق"
  },
  "RON": {
    "code": "RON",
    "fractional_ratio": "100",
    "fractional_unit": "Ban",
    "name": "New Leu (Romania)",
    "symbol": "L"
  },
  "RSD": {
    "code": "RSD",
    "fractional_ratio": "100",
    "fractional_unit": "Para",
    "name": "Dinar (Serbia)",
    "symbol": "дин. or din."
  },
  "RUB": {
    "code": "RUB",
    "fractional_ratio": "100",
    "fractional_unit": "Kopek",
    "name": "Ruble (Russia)",
    "symbol": "р."
  },
  "RWF": {
    "code": "RWF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Rwanda)",
    "symbol": "Fr"
  },
  "SAR": {
    "code": "SAR",
    "fractional_ratio": "100",
    "fractional_unit": "Halala",
    "name": "Riyal (Saudi Arabia)",
    "symbol": "ر.س"
  },
  "SBD": {
    "code": "SBD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Solomon Islands)",
    "symbol": "$"
  },
  "SCR": {
    "code": "SCR",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Rupee (Seychelles)",
    "symbol": "₨"
  },
  "SDG": {
    "code": "SDG",
    "fractional_ratio": "100",
    "fractional_unit": "Piastre",
    "name": "Pound (Sudan)",
    "symbol": "£"
  },
  "SEK": {
    "code": "SEK",
    "fractional_ratio": "100",
    "fractional_unit": "Öre",
    "name": "Krona (Sweden)",
    "symbol": "kr"
  },
  "SGD": {
    "code": "SGD",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Dollar (Singapore)",
    "symbol": ""
  },
  "SHP": {
    "code": "SHP",
    "fractional_ratio": "100",
    "fractional_unit": "Penny",
    "name": "Pound (Saint Helena)",
    "symbol": "£"
  },
  "SLL": {
    "code": "SLL",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Leone Leone (Sierra)",
    "symbol": "Le"
  },
  "SOS": {
    "code": "SOS",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Shilling (Somalia)",
    "symbol": "Sh"
  },
  "SPL": {
    "code": "SPL",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Luigino (Seborga)",
    "symbol": ""
  },
  "SRD": {
    "code": "SRD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Suriname)",
    "symbol": "$"
  },
  "SSP": {
    "code": "SSP",
    "fractional_ratio": "100",
    "fractional_unit": "Piaster",
    "name": "Pound (South Sudan)",
    "symbol": "£"
  },
  "STD": {
    "code": "STD",
    "fractional_ratio": "100",
    "fractional_unit": "Cêntimo",
    "name": "Dobra (Sao Tome)",
    "symbol": "Db"
  },
  "SVC": {
    "code": "SVC",
    "fractional_ratio": "100",
    "fractional_unit": "Centavo",
    "name": "Colon (El Salvador)",
    "symbol": "₡"
  },
  "SYP": {
    "code": "SYP",
    "fractional_ratio": "100",
    "fractional_unit": "Piastre",
    "name": "Pound (Syria)",
    "symbol": "£ or ل.س"
  },
  "SZL": {
    "code": "SZL",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Lilangeni (Swaziland)",
    "symbol": "L"
  },
  "THB": {
    "code": "THB",
    "fractional_ratio": "100",
    "fractional_unit": "Satang",
    "name": "Baht (Thailand)",
    "symbol": "฿"
  },
  "TJS": {
    "code": "TJS",
    "fractional_ratio": "100",
    "fractional_unit": "Diram",
    "name": "Somoni (Tajikistan)",
    "symbol": "ЅМ"
  },
  "TMT": {
    "code": "TMT",
    "fractional_ratio": "100",
    "fractional_unit": "Tennesi",
    "name": "Manat (Turkmenistan)",
    "symbol": "m"
  },
  "TND": {
    "code": "TND",
    "fractional_ratio": "1000",
    "fractional_unit": "Millime",
    "name": "Dinar (Tunisia)",
    "symbol": "د.ت"
  },
  "TOP": {
    "code": "TOP",
    "fractional_ratio": "100",
    "fractional_unit": "Seniti",
    "name": "Pa'anga (Tonga)",
    "symbol": "T$"
  },
  "TRY": {
    "code": "TRY",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Lira (Turkey)",
    "symbol": ""
  },
  "TTD": {
    "code": "TTD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (Trinidad and Tobago)",
    "symbol": "$"
  },
  "TVD": {
    "code": "TVD",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Dollar (Tuvalu)",
    "symbol": ""
  },
  "TWD": {
    "code": "TWD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "New Dollar (Taiwan)",
    "symbol": "$"
  },
  "TZS": {
    "code": "TZS",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Shilling (Tanzania)",
    "symbol": "Sh"
  },
  "UAH": {
    "code": "UAH",
    "fractional_ratio": "100",
    "fractional_unit": "Kopiyka",
    "name": "Hryvna (Ukraine)",
    "symbol": "₴"
  },
  "UGX": {
    "code": "UGX",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Shilling (Uganda)",
    "symbol": "Sh"
  },
  "USD": {
    "code": "USD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (United States)",
    "symbol": "$"
  },
  "UYU": {
    "code": "UYU",
    "fractional_ratio": "100",
    "fractional_unit": "Centésimo",
    "name": "Peso (Uruguay)",
    "symbol": "$"
  },
  "UZS": {
    "code": "UZS",
    "fractional_ratio": "100",
    "fractional_unit": "Tiyin",
    "name": "Som (Uzbekistan)",
    "symbol": "лв"
  },
  "VEF": {
    "code": "VEF",
    "fractional_ratio": "100",
    "fractional_unit": "Céntimo",
    "name": "Bolivar (Venezuela)",
    "symbol": "Bs F"
  },
  "VND": {
    "code": "VND",
    "fractional_ratio": "10",
    "fractional_unit": "Hào",
    "name": "Dong (Viet Nam)",
    "symbol": "₫"
  },
  "VUV": {
    "code": "VUV",
    "fractional_ratio": "1",
    "fractional_unit": "",
    "name": "Vatu (Vanuatu)",
    "symbol": "Vt"
  },
  "WST": {
    "code": "WST",
    "fractional_ratio": "100",
    "fractional_unit": "Sene",
    "name": "Tala (Samoa)",
    "symbol": "T"
  },
  "XAF": {
    "code": "XAF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Financial Cooperation in Central Africa)",
    "symbol": "Fr"
  },
  "XCD": {
    "code": "XCD",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Dollar (East Caribbean)",
    "symbol": "$"
  },
  "XDR": {
    "code": "XDR",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "International Monetary Fund (IMF)",
    "symbol": ""
  },
  "XOF": {
    "code": "XOF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (Financial Community of Africa)",
    "symbol": "Fr"
  },
  "XPF": {
    "code": "XPF",
    "fractional_ratio": "100",
    "fractional_unit": "Centime",
    "name": "Franc (French Pacific)",
    "symbol": "Fr"
  },
  "YER": {
    "code": "YER",
    "fractional_ratio": "100",
    "fractional_unit": "Fils",
    "name": "Rial (Yemen)",
    "symbol": "﷼"
  },
  "ZAR": {
    "code": "ZAR",
    "fractional_ratio": "100",
    "fractional_unit": "Cent",
    "name": "Rand (South Africa)",
    "symbol": "R"
  },
  "ZMK": {
    "code": "ZMK",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Kwacha (Zambia)",
    "symbol": ""
  },
  "ZWL": {
    "code": "ZWL",
    "fractional_ratio": 0,
    "fractional_unit": "",
    "name": "Dollar (Zimbabwe)",
    "symbol": ""
  }
}




