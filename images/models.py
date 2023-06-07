from django.contrib.gis.db import models as gis_models
from django.db import models
from django.utils.translation import gettext_lazy as _
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField

from hashid_field.field import HashidAutoField


class ImageManager(models.Manager):
    pass


class Image(models.Model):
    id = HashidAutoField(prefix='image_', primary_key=True)
    thickness = models.IntegerField(_("Thickness in [mm]"))
    corners = gis_models.PolygonField(_("Corners coordinates"), geography=False)
    path = models.FileField()
    type = models.CharField(max_length=50, default='.png')
    file_type = models.CharField(max_length=5)
    verified = models.BooleanField(default=False)
    created = CreationDateTimeField()
    modified = ModificationDateTimeField()
    objects = ImageManager()

    class Meta:
        verbose_name: str = 'Image'
        verbose_name_plural: str = 'Images'
        ordering = ("-created",)


