from dal import autocomplete

from ..models import Timezone


class TimezoneAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Timezone Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Timezone.objects.none()

        qs = Timezone.objects.all()

        country = self.forwarded.get('country', None)
        if country:
            qs = qs.filter(country=country)

        if self.q:
            qs = qs.filter(name_id__icontains=self.q)

        return qs
