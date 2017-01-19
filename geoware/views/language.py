from dal import autocomplete

from ..models import Language


class LanguageAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Language Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Language.objects.none()

        qs = Language.objects.all()

        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs
