from api.v1.team.serializers.projects import EmployeeProjectSerializer
from api.v1.team.serializers.teams import EmployeeTeamSerializer
from apps.employee.models.education import Education
from apps.employee.models.employee import Employee
from apps.employee.models.favorite import FavoriteEmployee
from apps.employee.models.interest import Interest
from apps.employee.models.skills import Skill
from rest_framework import serializers


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("id", "name")


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ("id", "name")


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "type",
            "organization",
            "beginning",
            "graduation",
            "additional",
        )


class SubordinatesSerializer(serializers.ModelSerializer):
    subordinates = serializers.SerializerMethodField()

    class Meta:
        model = Employee
        fields = (
            "id",
            "firstname",
            "lastname",
            "image",
            "position",
            "department",
            "subordinates",
        )

    def get_subordinates(self, obj):
        print(self.context)
        # Get current depth from context and increase it
        current_depth = self.context.get("depth", 1)

        # Define maximum depth
        max_depth = 3

        if current_depth >= max_depth:
            return []  # Return empty list if max depth is reached

        # Pass increased depth into context
        context = self.context.copy()
        context["depth"] = current_depth + 1

        serializer = SubordinatesSerializer(
            obj.subordinates.all(), many=True, context=context
        )
        return serializer.data


class MemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        fields = (
            "id",
            "firstname",
            "lastname",
            "image",
            "position",
            "department",
        )


class LeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "firstname", "lastname", "image")


class FavoriteSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source="subscriber.id")
    firstname = serializers.CharField(source="subscriber.firstname")
    lastname = serializers.CharField(source="subscriber.lastname")
    image = serializers.ImageField(source="subscriber.image")
    position = serializers.CharField(source="subscriber.position")
    department = serializers.CharField(source="subscriber.department")

    class Meta:
        model = FavoriteEmployee
        fields = (
            "id",
            "firstname",
            "lastname",
            "image",
            "position",
            "department",
        )


class EmployeeListSerializer(serializers.ModelSerializer):
    subordinates = SubordinatesSerializer(
        many=True,
    )
    address = serializers.CharField(source="address.full_address")

    class Meta:
        model = Employee
        fields = (
            "id",
            "firstname",
            "lastname",
            "image",
            "position",
            "address",
            "department",
            "subordinates",
        )


class EmployeeDetailSerializer(serializers.ModelSerializer):
    skills = SkillsSerializer(many=True)
    interest = InterestSerializer(many=True)
    address = serializers.CharField(source="address.full_address")
    leadership = LeaderSerializer()
    education = EducationSerializer(many=True)
    teams = EmployeeTeamSerializer(many=True)
    projects = EmployeeProjectSerializer(many=True)
    favorites = FavoriteSerializer(many=True)
    deputy = MemberSerializer()

    class Meta:
        model = Employee
        fields = (
            "id",
            "firstname",
            "lastname",
            "image",
            "position",
            "staff",
            "availability",
            "absence",
            "deputy",
            "format_work",
            "dey_week",
            "work_time",
            "email",
            "telephone",
            "telephone_work",
            "default_telephone",
            "telegram",
            "address",
            "leadership",
            "interest",
            "skills",
            "biography",
            "hobby",
            "success",
            "favorites",
            "education",
            "teams",
            "projects",
        )


class UpdateEmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("firstname", "lastname", "image", "position", "address")

    def update(self, instance, validated_data):

        instance.firstname = validated_data.get(
            "firstname", instance.firstname
        )
        instance.lastname = validated_data.get("lastname", instance.lastname)
        instance.image = validated_data.get("image", instance.image)
        instance.position = validated_data.get("position", instance.position)
        instance.address = validated_data.get("address", instance.address)
        instance.department = validated_data.get(
            "department", instance.department
        )
        instance.save()
        return super().update(instance, validated_data)
