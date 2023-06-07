from rest_framework import viewsets

from images.models import Image
from images.serializers import ImageSerializer
from images.filter import ImageFilter


class ImageViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides an interface for handling CRUD operations on Folder objects. It uses the FolderSerializer
    for creating and updating folders, and the FolderSerializerDetail for retrieving and destroying folders.

    If a folder is owned by a user, all its children will also be owned by that user.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filterset_class = ImageFilter
