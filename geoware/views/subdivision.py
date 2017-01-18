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

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
