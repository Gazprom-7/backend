from rest_framework import serializers
from apps.team.models.team import Team


class EmployeeTeamSerializer(serializers.ModelSerializer):
    leader = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ("id", "name", "leader")

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderSerializer

        return LeaderSerializer(obj.leader).data
