from rest_framework import serializers
from apps.team.models.team import Project
from api.v1.team.serializers.teams import TeamInProjectSerializer


class EmployeeProjectSerializer(serializers.ModelSerializer):
    leader = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "leader",
        )

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderSerializer

        return LeaderSerializer(obj.leader).data


class ProjectListSerializer(serializers.ModelSerializer):
    teams = TeamInProjectSerializer(source="teams_projects", many=True)
    leader = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ("id", "name", "leader", "teams")

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderWithOutImageSerializer

        return LeaderWithOutImageSerializer(obj.leader).data
