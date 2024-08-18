from django.db import models
from django.utils.translation import gettext_lazy as _


class Interest(models.Model):
    name = models.CharField(_("Название интереса"), max_length=127)

    def __str__(self):
        return self.name
