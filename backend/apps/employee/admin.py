from django.contrib import admin

from .models.address import Address
from .models.education import Education
from .models.employee import Employee


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass
