from django.db import models
from django.utils.translation import gettext_lazy as _


class Education(models.Model):
    degree = models.CharField(_("Уровень образования"), max_length=127)
    organization = models.CharField(_("Учебное заведение"), max_length=127)
    year = models.IntegerField(_("Год"), null=True, blank=True)
    additional = models.BooleanField(
        _("Дополнительное образование"), null=True, blank=True, default=False
    )

    def __str__(self):
        return self.organization
