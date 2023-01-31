from hashid_field.rest import HashidSerializerCharField
from rest_framework import serializers

from images.models import Image


class ImageSerializer(serializers.ModelSerializer):
    id = HashidSerializerCharField(read_only=True, required=False)

    class Meta(object):
        model = Image
        fields = '__all__'
