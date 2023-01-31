from django.db import models
from django_extensions.db.models import TimeStampedModel
from hashid_field.field import HashidAutoField


class ImageManager(models.Manager):
    pass


class Image(TimeStampedModel):
    id = HashidAutoField(prefix='image_', primary_key=True)
    length = models.IntegerField()
    width = models.IntegerField()
    thickness = models.IntegerField()
    useless_length = models.IntegerField()
    useless_width = models.IntegerField()
    path = models.FileField()
    type = models.CharField(max_length=50)
    objects = ImageManager()

    class Meta:
        verbose_name: str = 'Image'
        verbose_name_plural: str = 'Images'
        ordering = ("-created",)
