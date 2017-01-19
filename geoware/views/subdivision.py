from dal import autocomplete

from ..models import Subdivision


class SubdivisionAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Subdivision Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Subdivision.objects.none()

        qs = Subdivision.objects.all()

        division = self.forwarded.get('division', None)
        if division:
            qs = qs.filter(division=division)

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
