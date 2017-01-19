from dal import autocomplete

from ..models import City


class CityAutocompleteView(autocomplete.Select2QuerySetView):
    """
    City Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return City.objects.none()

        qs = City.objects.all()

        country = self.forwarded.get('country', None)
        if country:
            qs = qs.filter(country=country)

        division = self.forwarded.get('division', None)
        if division:
            qs = qs.filter(division=division)

        subdivision = self.forwarded.get('subdivision', None)
        if division:
            qs = qs.filter(subdivision=subdivision)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
