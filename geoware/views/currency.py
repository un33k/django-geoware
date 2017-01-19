from dal import autocomplete

from ..models import Currency


class CurrencyAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Currency Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Currency.objects.none()

        qs = Currency.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
