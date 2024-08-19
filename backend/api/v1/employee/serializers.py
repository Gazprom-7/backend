from api.v1.team.serializers.projects import EmployeeProjectSerializer
from api.v1.team.serializers.teams import EmployeeTeamWithOutLeaderSerializer
from apps.employee.models.education import Education
from apps.employee.models.employee import Employee
from apps.employee.models.favorite import FavoriteEmployee
from apps.employee.models.interest import Interest
from apps.employee.models.skills import Skill
from rest_framework import serializers


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ("core", "language")


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = ("name",)


class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = (
            "degree",
            "organization",
            "year",
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
        # Get current depth from context and increase it
        current_depth = self.context.get("depth", 1)

        # Define maximum depth
        max_depth = 2

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


class LeaderWithOutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            "id",
            "firstname",
            "lastname",
        )


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
    department = serializers.SerializerMethodField()

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

    def get_department(self, obj):
        return None


class EmployeeDetailSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="firstname")
    skills = SkillsSerializer(many=True)
    interest = InterestSerializer(many=True)
    city = serializers.CharField(source="address.full_address")
    lead = serializers.SerializerMethodField()
    education = EducationSerializer(many=True)
    teams = EmployeeTeamWithOutLeaderSerializer(many=True)
    projects = EmployeeProjectSerializer(many=True)
    favorites = FavoriteSerializer(many=True)
    status = serializers.SerializerMethodField()
    contact = serializers.SerializerMethodField()
    work_format = serializers.CharField(source="format_work")
    achievements = serializers.CharField(source="success")
    about = serializers.CharField(source="biography")

    class Meta:
        model = Employee
        fields = (
            "id",
            "name",
            "lastname",
            "image",
            "position",
            "staff",
            "status",
            "work_format",
            "work_time",
            "city",
            "contact",
            "lead",
            "teams",
            "projects",
            "education",
            "interest",
            "skills",
            "about",
            "hobby",
            "achievements",
            "favorites",
        )

    def get_contact(self, obj):
        return {
            "email": obj.email,
            "telephone": obj.telephone,
            "telephone_work": obj.telephone_work,
            "telegram": obj.telegram,
        }

    def get_status(self, obj):
        if obj.deputy is None:
            return {
                "description": obj.availability,
                "date": obj.absence,
                "replacement": None,
            }

        return {
            "description": obj.availability,
            "date": obj.absence,
            "replacement": {
                "id": obj.deputy.id,
                "name": obj.deputy.firstname,
                "lastname": obj.deputy.lastname,
            },
        }

    def get_lead(self, obj):
        if obj.leadership is not None:
            return {
                "id": obj.leadership.id,
                "name": obj.leadership.firstname,
                "lastname": obj.leadership.lastname,
            }
        return None


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


class AddEmployeeSerializer(serializers.Serializer):
    member = serializers.IntegerField()
