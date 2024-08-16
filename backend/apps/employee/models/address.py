from django.db import models
from django.utils.translation import gettext_lazy as _


class Address(models.Model):
    country = models.CharField(_("Страна"), max_length=31)
    timezone = models.CharField(_("Часовой пояс"), max_length=31)

    @property
    def full_address(self):
        return f"{self.country}, {self.timezone}"

    def __str__(self):
        return self.full_address
