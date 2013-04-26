from django.contrib import admin
from ..models import Continent
from ..models import Country
from ..models import Region
from ..models import Subregion
from ..models import City
from ..models import District
from ..models import Ocean
from ..models import Language
from ..models import Currency
from ..models import Timezone
from ..models import Altname

from continent import ContinentAdmin
from country import CountryAdmin
from region import RegionAdmin
from subregion import SubregionAdmin
from city import CityAdmin
from district import DistrictAdmin
from ocean import OceanAdmin
from language import LanguageAdmin
from currency import CurrencyAdmin
from timezone import TimezoneAdmin
from altname import AltnameAdmin

admin.site.register(Ocean, OceanAdmin)
admin.site.register(Currency, CurrencyAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Continent, ContinentAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Region, RegionAdmin)
admin.site.register(Subregion, SubregionAdmin)
admin.site.register(City, CityAdmin)
admin.site.register(District, DistrictAdmin)
admin.site.register(Timezone, TimezoneAdmin)
admin.site.register(Altname, AltnameAdmin)




