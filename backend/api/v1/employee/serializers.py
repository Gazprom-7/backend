from rest_framework import serializers
from apps.employee.models.employee import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="address.country", read_only=True)

    class Meta:
        model = Employee
        fields = (
            "firstname",
            "lastname",
            "image",
            "position",
            "city",
            "department",
        )


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id",
            "firstname",
            "lastname",
        )
