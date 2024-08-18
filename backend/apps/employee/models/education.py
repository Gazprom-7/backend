from django.db import models
from django.utils.translation import gettext_lazy as _


class Education(models.Model):
    type = models.CharField(_("Тип образования"), max_length=31)
    organization = models.CharField(_("Учебное заведение"), max_length=127)
    beginning = models.DateField(_("Начало учебы"), null=True, blank=True)
    graduation = models.DateField(_("Выпуск"), null=True, blank=True)
    additional = models.BooleanField(
        _("Дополнительное образование"), null=True, blank=True
    )

    def __str__(self):
        return self.organization
