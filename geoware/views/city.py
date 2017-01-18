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

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
