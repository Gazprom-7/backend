from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)

        data["id"] = self.user.id
        data["name"] = self.user.employee.firstname
        data["lastname"] = self.user.employee.lastname
        if self.user.employee.image:
            data["image"] = self.user.employee.image.url
        else:
            data["image"] = None

        return data
