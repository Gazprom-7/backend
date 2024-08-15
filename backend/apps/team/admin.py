from django.contrib import admin

from .models.projects import Project
from .models.team import Team


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    pass


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    pass
