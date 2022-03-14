"""Users Admin model."""

# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Models
from cride.users.models import User
from cride.users.models import Profile


class CustomUserAdmin(UserAdmin):
    """User Admin Model."""

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_client', 'is_staff', 'created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile Admin Model."""

    list_display = ('user', 'reputation', 'rides_taken', 'rides_offered')
    search_field = ('user__username', 'user__email', 'user__first_name', 'user__last_name')
    list_filter = ('reputation',)

admin.site.register(User, CustomUserAdmin)

