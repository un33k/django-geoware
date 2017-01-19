from dal import autocomplete

from ..models import Altname


class AltnameAutocompleteView(autocomplete.Select2QuerySetView):
    """
    Altname Autocomplete view.
    """
    def get_queryset(self):
        if not self.request.user.is_authenticated():
            return Altname.objects.none()

        qs = Altname.objects.all()

        ref_geoname_id = self.forwarded.get('geoname_id', None)
        if ref_geoname_id:
            qs = qs.filter(ref_geoname_id=ref_geoname_id)

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs
