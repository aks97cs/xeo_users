from django.contrib import admin
from service.models import UserInfo
from service.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = "info"


class UserAdmin(BaseUserAdmin):
    inlines = (UserInfoInline,)


# admin.site.unregister(User)
admin.site.register(User, UserAdmin)
