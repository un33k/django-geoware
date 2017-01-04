import os

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

GEOWARE_USING_GIS = getattr(settings, 'GEOWARE_USING_GIS', False)

GEOWARE_DATA_DIR = getattr(settings, 'GEOWARE_DATA_DIR',
                os.path.abspath(os.path.join(os.path.expanduser("~"), '.geoware_cache_dir')))


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
    'AD', 'AE', 'AF', 'AG', 'AI', 'AL', 'AM', 'AO',
    'AQ', 'AR', 'AS', 'AT', 'AU', 'AW', 'AZ', 'BA',
    'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ',
    'BM', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BY',
    'BZ', 'CA', 'CC', 'CF', 'CG', 'CH', 'CI', 'CK',
    'CL', 'CM', 'CN', 'CO', 'CR', 'CU', 'CV', 'CX',
    'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ',
    'EC', 'EE', 'EG', 'EH', 'ER', 'ES', 'ET', 'FI',
    'FJ', 'FK', 'FM', 'FO', 'FR', 'GA', 'GB', 'GD',
    'GE', 'GF', 'GH', 'GI', 'GL', 'GM', 'GN', 'GP',
    'GQ', 'GR', 'GS', 'GT', 'GU', 'GW', 'GY', 'HK',
    'HM', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL',
    'IN', 'IO', 'IQ', 'IR', 'IS', 'IT', 'JM', 'JO',
    'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KP',
    'KR', 'KW', 'KY', 'KZ', 'LA', 'LB', 'LC', 'LI',
    'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA',
    'MC', 'MD', 'MG', 'MH', 'ML', 'MN', 'MM', 'MO',
    'MP', 'MQ', 'MR', 'MS', 'MT', 'MU', 'MV', 'MW',
    'MX', 'MY', 'MZ', 'NA', 'NC', 'NE', 'NF', 'NG',
    'NI', 'NL', 'NO', 'NP', 'NR', 'NU', 'NZ', 'OM',
    'PA', 'PE', 'PF', 'PG', 'PH', 'PK', 'PL', 'PM',
    'PN', 'PR', 'PT', 'PW', 'PY', 'QA', 'RE', 'RO',
    'RU', 'RW', 'SA', 'SB', 'SC', 'SD', 'SE', 'SG',
    'SH', 'SI', 'SJ', 'SK', 'SL', 'SM', 'SN', 'SO',
    'SR', 'ST', 'SV', 'SY', 'SZ', 'TC', 'TD', 'TF',
    'TG', 'TH', 'TJ', 'TK', 'TM', 'TN', 'TO', 'TR',
    'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'UM', 'US',
    'UY', 'UZ', 'VA', 'VC', 'VE', 'VG', 'VI', 'VN',
    'VU', 'WF', 'WS', 'YE', 'YT', 'ZA', 'ZM', 'ZW',
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
    ('OC', _('Oceania')),
    ('EU', _('Europe')),
    ('AF', _('Africa')),
    ('NA', _('North America')),
    ('AN', _('Antarctica')),
    ('SA', _('South America')),
    ('AS', _('Asia')),
)

GEOWARE_OCEAN_CHOICES = (
    ('Arctic', _('Arctic')),
    ('Atlantic', _('Atlantic')),
    ('Indian', _('Indian')),
    ('Pacific', _('Pacific')),
    ('Southern', _('Southern')),
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
    ('af',      _('Afrikaans')),
    ('af-ZA',   _('Afrikaans (South Africa)')),
    ('ar',      _('Arabic')),
    ('ar-AE',   _('Arabic (UAE)')),
    ('ar-BH',   _('Arabic (Bahrain)')),
    ('ar-DZ',   _('Arabic (Algeria)')),
    ('ar-EG',   _('Arabic (Egypt)')),
    ('ar-IQ',   _('Arabic (Iraq)')),
    ('ar-JO',   _('Arabic (Jordan)')),
    ('ar-KW',   _('Arabic (Kuwait)')),
    ('ar-LB',   _('Arabic (Lebanon)')),
    ('ar-LY',   _('Arabic (Libya)')),
    ('ar-MA',   _('Arabic (Morocco)')),
    ('ar-OM',   _('Arabic (Oman)')),
    ('ar-QA',   _('Arabic (Qatar)')),
    ('ar-SA',   _('Arabic (Saudi Arabia)')),
    ('ar-SY',   _('Arabic (Syria)')),
    ('ar-TN',   _('Arabic (Tunisia)')),
    ('ar-YE',   _('Arabic (Yemen)')),
    ('az',      _('Azeri')),
    ('az-AZ',   _('Azeri (Azerbaijan)')),
    ('be',      _('Belarusian')),
    ('be-BY',   _('Belarusian (Belarus)')),
    ('bg',      _('Bulgarian')),
    ('bg-BG',   _('Bulgarian (Bulgaria)')),
    ('bs-BA',   _('Bosnian (Bosnia and Herzegovina)')),
    ('ca',      _('Catalan')),
    ('ca-ES',   _('Catalan (Spain)')),
    ('cs',      _('Czech')),
    ('cs-CZ',   _('Czech (Czech Republic)')),
    ('cy',      _('Welsh')),
    ('cy-GB',   _('Welsh (United Kingdom)')),
    ('da',      _('Danish')),
    ('da-DK',   _('Danish (Denmark)')),
    ('de',      _('German')),
    ('de-AT',   _('German (Austria)')),
    ('de-CH',   _('German (Switzerland)')),
    ('de-DE',   _('German (Germany)')),
    ('de-LI',   _('German (Liechtenstein)')),
    ('de-LU',   _('German (Luxembourg)')),
    ('dv',      _('Divehi')),
    ('dv-MV',   _('Divehi (Maldives)')),
    ('el',      _('Greek')),
    ('el-GR',   _('Greek (Greece)')),
    ('en',      _('English')),
    ('en-AU',   _('English (Australia)')),
    ('en-BZ',   _('English (Belize)')),
    ('en-CA',   _('English (Canada)')),
    ('en-CB',   _('English (Caribbean)')),
    ('en-GB',   _('English (United Kingdom)')),
    ('en-IE',   _('English (Ireland)')),
    ('en-JM',   _('English (Jamaica)')),
    ('en-NZ',   _('English (New Zealand)')),
    ('en-PH',   _('English (The Philippines)')),
    ('en-TT',   _('English (Trinidad and Tobago)')),
    ('en-US',   _('English (United States)')),
    ('en-VC',   _('English (Saint Vincent and the Grenadines)')),
    ('en-VG',   _('English (British Virgin Islands)')),
    ('en-ZA',   _('English (South Africa)')),
    ('en-ZW',   _('English (Zimbabwe)')),
    ('eo',      _('Esperanto')),
    ('es',      _('Spanish')),
    ('es-AR',   _('Spanish (Argentina)')),
    ('es-BO',   _('Spanish (Bolivia)')),
    ('es-CL',   _('Spanish (Chile)')),
    ('es-CO',   _('Spanish (Colombia)')),
    ('es-CR',   _('Spanish (Costa Rica)')),
    ('es-DO',   _('Spanish (Dominican Republic)')),
    ('es-EC',   _('Spanish (Ecuador)')),
    ('es-ES',   _('Spanish (Castilian)')),
    ('es-ES',   _('Spanish (Spain)')),
    ('es-GT',   _('Spanish (Guatemala)')),
    ('es-HN',   _('Spanish (Honduras)')),
    ('es-MX',   _('Spanish (Mexico)')),
    ('es-NI',   _('Spanish (Nicaragua)')),
    ('es-PA',   _('Spanish (Panama)')),
    ('es-PE',   _('Spanish (Peru)')),
    ('es-PR',   _('Spanish (Puerto Rico)')),
    ('es-PY',   _('Spanish (Paraguay)')),
    ('es-SV',   _('Spanish (El Salvador)')),
    ('es-UY',   _('Spanish (Uruguay)')),
    ('es-VE',   _('Spanish (Venezuela)')),
    ('et',      _('Estonian')),
    ('et-EE',   _('Estonian (Estonia)')),
    ('eu',      _('Basque')),
    ('eu-ES',   _('Basque (Spain)')),
    ('fa',      _('Farsi')),
    ('fa-IR',   _('Farsi (Iran)')),
    ('fi',      _('Finnish')),
    ('fi-FI',   _('Finnish (Finland)')),
    ('fo',      _('Faroese')),
    ('fo-FO',   _('Faroese (Faroe Islands)')),
    ('fr',      _('French')),
    ('fr-BE',   _('French (Belgium)')),
    ('fr-CA',   _('French (Canada)')),
    ('fr-CH',   _('French (Switzerland)')),
    ('fr-FR',   _('French (France)')),
    ('fr-LU',   _('French (Luxembourg)')),
    ('fr-MC',   _('French (Monaco)')),
    ('fr-WF',   _('French (Futuna)')),
    ('fud',     _('Futunian (Futuna)')),
    ('gl',      _('Galician')),
    ('gl-ES',   _('Galician (Spain)')),
    ('gu',      _('Gujarati')),
    ('gu-IN',   _('Gujarati (India)')),
    ('he',      _('Hebrew')),
    ('he-IL',   _('Hebrew (Israel)')),
    ('hi',      _('Hindi')),
    ('hi-IN',   _('Hindi (India)')),
    ('hr',      _('Croatian')),
    ('hr-BA',   _('Croatian (Bosnia and Herzegovina)')),
    ('hr-HR',   _('Croatian (Croatia)')),
    ('hu',      _('Hungarian')),
    ('hu-HU',   _('Hungarian (Hungary)')),
    ('hy',      _('Armenian')),
    ('hy-AM',   _('Armenian (Armenia)')),
    ('id',      _('Indonesian')),
    ('id-ID',   _('Indonesian (Indonesia)')),
    ('is',      _('Icelandic')),
    ('is-IS',   _('Icelandic (Iceland)')),
    ('it',      _('Italian')),
    ('it-CH',   _('Italian (Switzerland)')),
    ('it-IT',   _('Italian (Italy)')),
    ('ja',      _('Japanese')),
    ('ja-JP',   _('Japanese (Japan)')),
    ('ka',      _('Georgian')),
    ('ka-GE',   _('Georgian (Georgia)')),
    ('kk',      _('Kazakh')),
    ('kk-KZ',   _('Kazakh (Kazakhstan)')),
    ('kn',      _('Kannada')),
    ('kn-IN',   _('Kannada (India)')),
    ('ko',      _('Korean')),
    ('ko-KR',   _('Korean (Korea)')),
    ('kok',     _('Konkani')),
    ('kok-IN',  _('Konkani (India)')),
    ('ky',      _('Kyrgyz')),
    ('ky-KG',   _('Kyrgyz (Kyrgyzstan)')),
    ('lt',      _('Lithuanian')),
    ('lt-LT',   _('Lithuanian (Lithuania)')),
    ('lv',      _('Latvian')),
    ('lv-LV',   _('Latvian (Latvia)')),
    ('mi',      _('Maori')),
    ('mi-NZ',   _('Maori (New Zealand)')),
    ('mk',      _('Macedonian')),
    ('mk-MK',   _('Macedonian (Republic of Macedonia)')),
    ('mn',      _('Mongolian')),
    ('mn-MN',   _('Mongolian (Mongolia)')),
    ('mr',      _('Marathi')),
    ('mr-IN',   _('Marathi (India)')),
    ('ms',      _('Malay')),
    ('ms-BN',   _('Malay (Brunei Darussalam)')),
    ('ms-MY',   _('Malay (Malaysia)')),
    ('mt',      _('Maltese')),
    ('mt-MT',   _('Maltese (Malta)')),
    ('nb',      _('Norwegian Bokmal')),
    ('nb-NO',   _('Norwegian Bokmal (Norway)')),
    ('nl',      _('Dutch')),
    ('nl-BE',   _('Dutch (Belgium)')),
    ('nl-NL',   _('Dutch (Netherlands)')),
    ('nn-NO',   _('Norwegian Nynorsk (Norway)')),
    ('ns',      _('Northern Sotho')),
    ('ns-ZA',   _('Northern Sotho (South Africa)')),
    ('pa',      _('Punjabi')),
    ('pa-IN',   _('Punjabi (India)')),
    ('pl',      _('Polish')),
    ('pl-PL',   _('Polish (Poland)')),
    ('ps',      _('Pashto')),
    ('ps-AR',   _('Pashto (Afghanistan)')),
    ('pt',      _('Portuguese')),
    ('pt-BR',   _('Portuguese (Brazil)')),
    ('pt-PT',   _('Portuguese (Portugal)')),
    ('qu',      _('Quechua')),
    ('qu-BO',   _('Quechua (Bolivia)')),
    ('qu-EC',   _('Quechua (Ecuador)')),
    ('qu-PE',   _('Quechua (Peru)')),
    ('ro',      _('Romanian')),
    ('ro-RO',   _('Romanian (Romania)')),
    ('ru',      _('Russian')),
    ('ru-RU',   _('Russian (Russia)')),
    ('sa',      _('Sanskrit')),
    ('sa-IN',   _('Sanskrit (India)')),
    ('se',      _('Sami (Northern)')),
    ('se-FI',   _('Sami (Finland)')),
    ('se-NO',   _('Sami (Norway)')),
    ('se-SE',   _('Sami (Sweden)')),
    ('sk',      _('Slovak')),
    ('sk-SK',   _('Slovak (Slovakia)')),
    ('sl',      _('Slovenian')),
    ('sl-SI',   _('Slovenian (Slovenia)')),
    ('sq',      _('Albanian')),
    ('sq-AL',   _('Albanian (Albania)')),
    ('sr-BA',   _('Serbian (Bosnia and Herzegovina)')),
    ('sr-SP',   _('Serbian (Serbia and Montenegro)')),
    ('sv',      _('Swedish')),
    ('sv-FI',   _('Swedish (Finland)')),
    ('sv-SE',   _('Swedish (Sweden)')),
    ('sw',      _('Swahili')),
    ('sw-KE',   _('Swahili (Kenya)')),
    ('syr',     _('Syriac')),
    ('syr-SY',  _('Syriac (Syria)')),
    ('ta',      _('Tamil')),
    ('ta-IN',   _('Tamil (India)')),
    ('te',      _('Telugu')),
    ('te-IN',   _('Telugu (India)')),
    ('th',      _('Thai')),
    ('th-TH',   _('Thai (Thailand)')),
    ('tl',      _('Tagalog')),
    ('tl-PH',   _('Tagalog (The Philippines)')),
    ('tn',      _('Tswana')),
    ('tn-ZA',   _('Tswana (South Africa)')),
    ('tr',      _('Turkish')),
    ('tr-TR',   _('Turkish (Turkey)')),
    ('tt',      _('Tatar')),
    ('tt-RU',   _('Tatar (Russia)')),
    ('ts',      _('Tsonga')),
    ('uk',      _('Ukrainian')),
    ('uk-UA',   _('Ukrainian (Ukraine)')),
    ('ur',      _('Urdu')),
    ('ur-PK',   _('Urdu (Pakistan)')),
    ('uz',      _('Uzbek (Latin)')),
    ('uz-UZ',   _('Uzbek (Uzbekistan)')),
    ('vi',      _('Vietnamese')),
    ('vi-VN',   _('Vietnamese (Viet Nam)')),
    ('wls',     _('Wallisian (Noumea)')),
    ('xh',      _('Xhosa')),
    ('xh-ZA',   _('Xhosa (South Africa)')),
    ('zh',      _('Chinese')),
    ('zh-CN',   _('Chinese (Simplified)')),
    ('zh-HK',   _('Chinese (Hong Kong)')),
    ('zh-MO',   _('Chinese (Macau)')),
    ('zh-SG',   _('Chinese (Singapore)')),
    ('zh-TW',   _('Chinese (Traditional)')),
    ('zu',      _('Zulu')),
    ('zu-ZA',   _('Zulu (South Africa)')),
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
