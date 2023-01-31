from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from images.models import Image
from images.serializers import ImageSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """
    This endpoint provides an interface for handling CRUD operations on Folder objects. It uses the FolderSerializer
    for creating and updating folders, and the FolderSerializerDetail for retrieving and destroying folders.

    If a folder is owned by a user, all its children will also be owned by that user.
    """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    def create(self, request, *args, **kwargs):
        "Logica para capturar a image e os seu atributos"
        """
        Pillow, attrs 
        
        os attrs:  
        length = int
        width = int
        thickness = int
        useless_length = int
        useless_width = int
        path = Convert the pillow image to a byte array
        type = str
        
        """
        data = dict(
            length="int",
            width = "int",
            thickness = "int",
            useless_length = "int",
             useless_width = "int",
            path = "Convert the pillow image to a byte array",
            ype = "str"
        )
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
