from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.employee.models.employee import Employee


class Project(models.Model):
    name = models.CharField(_("Название проекта"), max_length=255)
    description = models.TextField(
        _("Описание проекта"), null=True, blank=True
    )
    leader = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="leaders_projects",
        verbose_name=_("Руководитель проекта"),
    )
    image = models.ImageField(
        _("Изображение проекта"),
        null=True,
        blank=True,
        upload_to="images/projects",
    )
    created = models.DateTimeField(_("Создано"), auto_now_add=True)
    ended = models.DateTimeField(_("Завершено"), null=True, blank=True)
    archived = models.BooleanField(_("Архивировано"), default=False)

    def __str__(self):
        return f'Название проекта: {self.name}'
