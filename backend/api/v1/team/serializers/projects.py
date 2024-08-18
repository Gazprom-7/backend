from rest_framework import serializers
from apps.team.models.team import Project


class EmployeeProjectSerializer(serializers.ModelSerializer):
    leader = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = (
            "id",
            "name",
            "description",
            "image",
            "leader",
        )

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderSerializer

        return LeaderSerializer(obj.leader).data
