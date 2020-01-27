from django.contrib import admin
from users.models import TenantUser
from tenant_users.permissions.models import UserTenantPermissions


# Register your models here.


@admin.register(TenantUser)
class UserProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(UserTenantPermissions)
class UserTenantPermissionsAdmin(admin.ModelAdmin):
    pass
