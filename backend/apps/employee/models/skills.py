from django.db import models
from django.utils.translation import gettext_lazy as _


class Skill(models.Model):
    core = models.CharField(_("Основное навык"), max_length=127)
    language = models.CharField(_("Язык программирования"), max_length=127)

    def __str__(self):
        return self.core
