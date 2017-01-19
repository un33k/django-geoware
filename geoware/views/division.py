from dal import autocomplete

from ..models import Division


class DivisionAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Division Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Division.objects.none()

        qs = Division.objects.all()

        country = self.forwarded.get('country', None)
        if country:
            qs = qs.filter(country=country)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
