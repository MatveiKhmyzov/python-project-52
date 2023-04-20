from django.db import models
from django.utils.translation import gettext as _


class Label(models.Model):
    name = models.CharField(verbose_name=_('Name'),
                            max_length=100,
                            unique=True)
    date_create = models.DateTimeField(verbose_name=_('Date of creation'),
                                       auto_now_add=True)

    def __str__(self):
        return self.name
