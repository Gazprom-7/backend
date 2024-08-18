from django.contrib import admin

from .models.address import Address
from .models.education import Education
from .models.employee import Employee
from .models.favorite import FavoriteEmployee
from .models.interest import Interest
from .models.skills import Skill


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(FavoriteEmployee)
class FavoriteEAdmin(admin.ModelAdmin):
    pass


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Interest)
class InterestAdmin(admin.ModelAdmin):
    pass
