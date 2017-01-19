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

        contenent = self.forwarded.get('contenent', None)
        if contenent:
            qs = qs.filter(contenent=contenent)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
