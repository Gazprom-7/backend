from api.v1.employee.serializers import (
    EmployeeDetailSerializer,
    EmployeeListSerializer,
    UpdateEmployeeSerializer,
)
from apps.employee.models.employee import Employee
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ModelViewSet):
    http_method_names = ["get", "put", "patch",]
    queryset = Employee.objects.all()

    def get_serializer_class(self):
        if self.action == "retrieve":
            return EmployeeDetailSerializer
        if self.action == "update":
            return UpdateEmployeeSerializer
        return EmployeeListSerializer
