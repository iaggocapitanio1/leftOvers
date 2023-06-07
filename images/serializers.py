from hashid_field.rest import HashidSerializerCharField
from rest_framework_gis.serializers import GeoFeatureModelSerializer, GeometrySerializerMethodField
from rest_framework import serializers
from images.models import Image


class ImageSerializer(GeoFeatureModelSerializer):
    id = HashidSerializerCharField(read_only=True, required=False)
    area = serializers.SerializerMethodField()

    def get_area(self, obj):

        return obj.corners.area

    class Meta:
        model = Image
        geo_field = 'corners'
        fields = "__all__"
        auto_bbox = True
        extra_kwargs = dict(
            id={'read_only': True},
            verified={'read_only': True},
            file_type={'read_only': True},

        )
