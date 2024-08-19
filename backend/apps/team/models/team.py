from apps.employee.models.employee import Employee
from apps.team.models.projects import Project
from django.db import models
from django.utils.translation import gettext_lazy as _


class Team(models.Model):
    name = models.CharField(_("Название команды"), max_length=255)
    leader = models.ForeignKey(
        Employee,
        on_delete=models.SET_NULL,
        null=True,
        related_name="leaders_teams",
        verbose_name=_("Руководитель команды"),
    )
    created = models.DateTimeField(_("Создано"), auto_now_add=True)
    ended = models.DateTimeField(_("Завершено"), null=True, blank=True)
    archived = models.BooleanField(_("Архивировано"), default=False)
    projects = models.ManyToManyField(
        Project,
        related_name="teams_projects",
        verbose_name=_("Проекты"),
    )
    member = models.ManyToManyField(
        Employee,
        related_name="teams_member",
        verbose_name=_("Участники команды"),
        blank=True,
    )

    def __str__(self):
        return f"Название команды: {self.name}"
