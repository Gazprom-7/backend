from api.v1.employee.serializers import AddEmployeeSerializer
from api.v1.team.serializers.teams import (
    TeamDetailSerializer,
    TeamListSerializer,
)
from apps.employee.models.employee import Employee
from apps.team.models.team import Team
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()

    def get_serializer_class(self):
        if self.action in ["employees", "delete_employees"]:
            return AddEmployeeSerializer
        if self.action == "retrieve":
            return TeamDetailSerializer
        return TeamListSerializer

    @action(methods=["post"], detail=True,)
    def employees(self, request, pk=None, member_id=None):
        team = self.get_object()
        serializer = AddEmployeeSerializer(data=request.data)

        if serializer.is_valid():
            member_id = serializer.validated_data.get("member")
            try:
                member = Employee.objects.get(id=member_id)
                if member not in team.member.all():
                    team.member.add(member)
                    return Response(
                        {"status": "member added"}, status=status.HTTP_200_OK
                    )
                return Response(
                    {"error": "Member already in team"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Employee.DoesNotExist:
                return Response(
                    {"error": "Employee not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

    @employees.mapping.delete
    def delete_employees(self, request, pk=None, member_id=None):
        team = self.get_object()
        serializer = AddEmployeeSerializer(data=request.data)

        if serializer.is_valid():
            # member_id = serializer.validated_data.get("member")
            try:
                member = Employee.objects.get(id=member_id)
                if member in team.member.all():
                    team.member.remove(member)
                    return Response(
                        {"status": "member removed"}, status=status.HTTP_200_OK
                    )
                return Response(
                    {"error": "Member not in team"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            except Employee.DoesNotExist:
                return Response(
                    {"error": "Employee not found"},
                    status=status.HTTP_404_NOT_FOUND,
                )
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
