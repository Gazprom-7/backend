from apps.team.models.team import Team
from rest_framework import serializers


class EmployeeTeamWithOutLeaderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
        )


class EmployeeTeamSerializer(serializers.ModelSerializer):
    leader = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ("id", "name", "leader")

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderSerializer

        return LeaderSerializer(obj.leader).data


class TeamListSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ("id", "name", "member")

    def get_member(self, obj):
        from api.v1.employee.serializers import MemberSerializer

        return MemberSerializer(obj.member, many=True).data


class TeamDetailSerializer(serializers.ModelSerializer):
    member = serializers.SerializerMethodField()
    department = serializers.SerializerMethodField()
    leader = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "leader",
            "department",
            "member",
        )

    def get_member(self, obj):
        from api.v1.employee.serializers import MemberSerializer

        return MemberSerializer(obj.member, many=True).data

    def get_department(self, obj):
        # Получаем отделы всех участников команды
        departments = obj.member.values_list(
            "department", flat=True
        ).distinct()
        return list(departments)

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderSerializer

        return LeaderSerializer(obj.leader).data


class TeamInProjectSerializer(serializers.ModelSerializer):
    department = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = (
            "id",
            "name",
            "department",
        )

    def get_department(self, obj):
        # Получаем отделы всех участников команды
        departments = obj.member.values_list(
            "department", flat=True
        ).distinct()
        return list(departments)

    def get_leader(self, obj):
        from api.v1.employee.serializers import LeaderSerializer

        return LeaderSerializer(obj.leader).data
