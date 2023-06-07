from rest_framework_gis.filterset import GeoFilterSet
from rest_framework_gis.filters import GeometryFilter
from images.models import Image


class ImageFilter(GeoFilterSet):
    contains_properly = GeometryFilter(field_name='corners', lookup_expr='contains_properly')

    class Meta:
        model = Image
        fields = ['contains_properly']
