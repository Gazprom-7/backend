from django.contrib import admin
from models.address import Address


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    pass


