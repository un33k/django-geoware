from dal import autocomplete

from ..models import Country


class CountryAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Country Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Country.objects.none()

        qs = Country.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
