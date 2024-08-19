from rest_framework import viewsets

from apps.team.models.team import Project
from api.v1.team.serializers.projects import (
    ProjectListSerializer,
)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectListSerializer
