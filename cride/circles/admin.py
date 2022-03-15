"""Circles Admin Model."""

# Django
from django.contrib import admin

# Models
from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle Admin Model."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'is_verified',
        'is_limited',
        'members_limit'
    )

    search_fields = ('slug_name','name')

    list_filter = (
        'is_public',
        'is_verified',
        'is_limited'
    )

