# models.py
from django.db import models

from wagtail.images.models import Image, AbstractImage, AbstractRendition, WagtailImageField
from django.utils.translation import gettext_lazy as _

class CustomImage(AbstractImage):
    # Add any extra fields to image here

    # To add a caption field:
    file = WagtailImageField(
        verbose_name=_("file"),
        upload_to="media",
        width_field="width",
        height_field="height",
    )
    admin_form_fields = Image.admin_form_fields


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage, on_delete=models.CASCADE, related_name='renditions')
    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )