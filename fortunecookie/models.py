# Python
from __future__ import unicode_literals

# Six
import six

# Django
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

# Django-SortedM2M
from sortedm2m.fields import SortedManyToManyField


class BaseModel(models.Model):
    """Base model class to track created and modified timestamps."""

    class Meta:
        abstract = True

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


@python_2_unicode_compatible
class FortuneCookie(BaseModel):
    """Fortune cookie"""

    class Meta:
        ordering = ['fortune']

    fortune = models.CharField(
        max_length=255,
    )

    def __init__(self, *args, **kwargs):
        super(FortuneCookie, self).__init__(*args, **kwargs)

    def save(self, *args, **kwargs):
        super(FortuneCookie, self).save(*args, **kwargs)
